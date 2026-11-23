"""Transliterating ø, ł and similar letters in team names moves no other team mapping (23 Nov 2026).

normalize_team_name used to drop letters that NFKD does not decompose ("Bodø/Glimt" keyed as "bod glimt", so the
reviewed alias "Bodo/Glimt" never matched it). It now transliterates them. This test runs every mapping the
pipeline makes from a team name over every team name the repo knew on 23 Nov 2026 (tests/team_name_corpus.json,
built by scripts/team_name_corpus.py), once with the old normaliser and once with the new, and requires the
results to differ only where a name carries one of those letters:

  keys       which names share a canonical key (fixture-odds joins, alias lookups);
  history    team_research.history_team against each league's training names (the research identities);
  model      DixonColesModel.resolve_team against each league's training names (reviewed aliases, exact keys,
             then the fuzzy fallback).

Plus the reviewed UCL research aliases added the same day (LASK, Club Brugge).
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import unicodedata
import unittest
from unittest.mock import patch

import pandas as pd

import football_value_pipeline_v2_standalone as fvp
import team_research as tr

ROOT = Path(__file__).resolve().parents[1]
CORPUS = json.loads((Path(__file__).with_name('team_name_corpus.json')).read_text(encoding='utf-8'))
CHANGED = set('øØłŁđĐðÐıħĦŧŦæÆœŒßþÞ')


def legacy_normalize(name: str) -> str:
    """normalize_team_name before 23 Nov 2026, verbatim."""
    s = unicodedata.normalize("NFKD", str(name))
    s = "".join(ch for ch in s if not unicodedata.combining(ch)).lower()
    s = s.replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    tokens = [t for t in re.split(r"\s+", s.strip()) if t and t not in {
        "fc", "cf", "afc", "ac", "sc", "sv", "club", "de", "football", "calcio", "1904", "1899", "04", "05"}]
    return " ".join(tokens)


def training_names() -> dict:
    """Each league's training names: football-data.co.uk files for the domestic leagues, the CE3n fit file's
    European training names for UCL and UEL."""
    out = {}
    for key, league in fvp.LEAGUES.items():
        if key in ('UCL', 'UEL'):
            continue
        teams = set()
        for path in sorted((ROOT / '.football_cache').glob(f'*_{league.football_data_div}.csv')):
            frame = pd.read_csv(path, usecols=lambda c: c in ('HomeTeam', 'AwayTeam'), encoding='utf-8',
                                encoding_errors='replace')
            teams |= set(frame.stack().dropna().astype(str))
        out[key] = teams
    fits = json.loads((ROOT / 'research_ce3n_live_fits.json').read_text(encoding='utf-8'))
    out['UCL'], out['UEL'] = set(fits['european_names']['UCL']), set(fits['european_names']['UEL'])
    return out


def model_for(league_key, teams):
    model = object.__new__(fvp.DixonColesModel)
    model.league_key, model.teams = league_key, sorted(teams)
    model.team_to_idx = {t: i for i, t in enumerate(model.teams)}
    model._check_fitted = lambda: None
    return model


def mappings(names, leagues) -> dict:
    keys = {n: fvp.canonical_team_key(n) for n in names}
    history = {(k, n): tr.history_team(n, teams, k) for k, teams in leagues.items() for n in names}
    model = {}
    for k, teams in leagues.items():
        m = model_for(k, teams)
        model.update({(k, n): m.resolve_team(n)[0] for n in names})
    return {'keys': keys, 'history': history, 'model': model}


def partition(keys) -> set:
    groups = {}
    for name, key in keys.items():
        groups.setdefault(key, set()).add(name)
    return {frozenset(g) for g in groups.values()}


class TransliterationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.leagues = training_names()
        cls.new = mappings(CORPUS, cls.leagues)
        with patch.object(fvp, 'normalize_team_name', legacy_normalize):
            cls.old = mappings(CORPUS, cls.leagues)

    def test_corpus_is_the_repo_s_names(self):
        self.assertGreater(len(CORPUS), 700)
        self.assertTrue({'Bodø/Glimt', 'FK Bodø/Glimt', 'LASK', 'Club Brugge KV'} <= set(CORPUS))
        self.assertTrue(all(len(teams) > 15 for teams in self.leagues.values()))

    def test_letters_are_transliterated_not_dropped(self):
        self.assertEqual(fvp.normalize_team_name('Bodø/Glimt'), 'bodo glimt')
        self.assertEqual(fvp.normalize_team_name('Jagiellonia Białystok'), 'jagiellonia bialystok')
        self.assertEqual(fvp.normalize_team_name('Kasımpaşa'), 'kasimpasa')
        self.assertEqual(fvp.normalize_team_name('FC København'), 'kobenhavn')
        self.assertEqual(fvp.normalize_team_name('Fenerbahçe SK'), legacy_normalize('Fenerbahçe SK'))

    def test_only_names_with_those_letters_change_their_key_group(self):
        old, new = partition(self.old['keys']), partition(self.new['keys'])
        # No group splits: every old group sits inside one new group ...
        self.assertTrue(all(any(o <= g for g in new) for o in old), 'a key group split')
        # ... and every new group is one club's spellings coming together through a transliterated name.
        joined = new - old
        self.assertTrue(all(any(CHANGED & set(n) for n in g) for g in joined), joined)
        self.assertEqual(sorted(sorted(g) for g in joined), [
            ['Bodo Glimt', 'Bodo/Glimt', 'Bodø/Glimt', 'bodo glimt', 'bodoe glimt', 'bodø/glimt'],
            ['Jagiellonia Bialystok', 'Jagiellonia Białystok'],
            ['Lillestrom', 'Lillestrøm', 'lillestrøm']])

    def test_research_and_model_identities_move_only_for_those_names(self):
        for kind in ('history', 'model'):
            changed = {key: (self.old[kind][key], self.new[kind][key]) for key in self.old[kind]
                       if self.old[kind][key] != self.new[kind][key]}
            for (league, name), (before, after) in changed.items():
                self.assertTrue(CHANGED & set(name) or CHANGED & set(str(after)) or CHANGED & set(str(before)),
                                (kind, league, name, before, after))
            with self.subTest(kind):
                self.assertEqual(sorted((k, n, b, a) for (k, n), (b, a) in changed.items()), EXPECTED[kind])

    def test_ucl_live_check_names_now_resolve(self):
        teams = self.leagues['UCL']
        self.assertEqual(tr.history_team('Bodø/Glimt', teams, 'UCL'), 'FK Bodø/Glimt')
        model = model_for('UCL', teams)
        for name in ('Bodø/Glimt', 'Bodo/Glimt'):
            self.assertEqual(model.resolve_team(name)[0], 'FK Bodø/Glimt')
        self.assertEqual(tr.history_team('LASK', teams, 'UCL'), 'LASK Linz')
        self.assertEqual(tr.history_team('Club Brugge', teams, 'UCL'), 'Club Brugge KV')


# The only identities that move. "bodø/glimt" is the UEL training spelling, never a UCL fixture name; against
# the UCL names it now keys like "Bodo Glimt" and "bodo glimt": the research resolves it to the club, and the
# model, where a global alias covers the name and its target is not a UCL training name, refuses it instead of
# fuzzy-matching, exactly as it already did for those two spellings. Every spelling a UCL fixture has used
# ("Bodø/Glimt", "Bodo/Glimt") keeps the model's identity (reviewed UCL aliases, bbs_team_aliases.json).
EXPECTED = {'history': [('UCL', 'bodø/glimt', None, 'FK Bodø/Glimt')],
            'model': [('UCL', 'bodø/glimt', 'FK Bodø/Glimt', None)]}


if __name__ == '__main__':
    unittest.main()
