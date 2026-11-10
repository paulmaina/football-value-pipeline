"""Research v4: club friendlies are left out of the last-ten form (docs/plan.md, Phase 1).

Uses a real frozen forecast, TSG Hoffenheim v FC Schalke 04 (8 Nov 2026), whose ESPN
form held three club friendlies (Hoffenheim v Elversberg on 2 Oct, Austria Lustenau v
Schalke on 3 Oct and RW Oberhausen v Schalke on 24 Sep), and two real ESPN schedule
events. League, cup and European games must be unchanged, and forecasts frozen under
v1-v3 must still replay exactly under their own version.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path
import tempfile
import unittest

import pandas as pd

import evaluation_harness as eh
import team_research as tr

FIXTURE = json.loads((Path(__file__).with_name('fixtures') / 'friendly_form_forecast.json').read_text(encoding='utf-8'))
CUTOFF = tr.utc(FIXTURE['frozen']['observed_at_utc'])
REAL_FRIENDLIES = {('home', '2026-10-02', 'TSG Hoffenheim', 'SV Elversberg'),
                   ('away', '2026-10-03', 'Austria Lustenau', 'Schalke 04'),
                   ('away', '2026-09-24', 'RW Oberhausen', 'Schalke 04')}


def row():
    return copy.deepcopy(FIXTURE['row'])


def evidence(labelled=True):
    out = copy.deepcopy(FIXTURE['evidence'])
    if not labelled:  # as frozen before v4: ESPN rows carry no competition
        for rows in out['recent'].values():
            for r in rows:
                r.pop('competition', None)
    return out


def hda(context):
    m = {int(k): v for k, v in context['margin_distribution'].items()}
    return [sum(p for d, p in m.items() if d > 0), m[0], sum(p for d, p in m.items() if d < 0)]


def form_keys(side, version):
    rows = eh._used_rows(tr.research_inputs(row()), evidence(), CUTOFF, side, version)
    return [(r['date'][:10], r['home'], r['away'], r.get('competition')) for r in rows]


class FriendlyCompetitionTest(unittest.TestCase):
    def test_friendly_slugs(self):
        for slug in ('club.friendly', 'friendly.emirates_cup', 'esp.joan_gamper', ' Club.Friendly '):
            self.assertTrue(tr.is_friendly(slug), slug)
        # Competitive games, and rows with no ESPN competition (training history, Understat, pre-v4 ESPN rows).
        for slug in ('ger.1', 'ger.dfb_pokal', 'eng.league_cup', 'uefa.europa', 'uefa.europa.conf_qual',
                     'ned.supercup', 'fra.super_cup', None, ''):
            self.assertFalse(tr.is_friendly(slug), slug)

    def test_every_espn_competition_seen_live_is_classified_as_reviewed(self):
        labels = json.loads((Path(__file__).resolve().parents[1] / 'evaluation' / 'research_parity_latest_rule'
                             / 'espn_competitions.json').read_text(encoding='utf-8'))
        friendly = {e['league'] for events in labels.values() for e in events if tr.is_friendly(e['league'])}
        self.assertEqual(friendly, {'club.friendly', 'friendly.emirates_cup', 'esp.joan_gamper'})

    def test_schedule_rows_record_the_espn_competition(self):
        events = FIXTURE['schedule_events']
        out = tr.schedule_rows({'events': events}, pd.Timestamp('2026-11-09', tz='UTC'), 'espn schedule')
        self.assertEqual({(r['home'], r['away'], r['competition']) for r in out},
                         {('PFC Turan Tovuz', 'Fenerbahce', 'club.friendly'),
                          ('Bayer Leverkusen', 'VfB Stuttgart', 'ger.1')})
        self.assertIn('competition', tr.RESULT_FIELDS)
        view = tr.research_evidence({'recent': {'home': out}})
        self.assertEqual({r['competition'] for r in view['recent']['home']}, {'club.friendly', 'ger.1'})

    def test_an_event_without_a_league_keeps_no_competition(self):
        event = copy.deepcopy(FIXTURE['schedule_events'][0])
        event.pop('league')
        out = tr.schedule_rows({'events': [event]}, pd.Timestamp('2026-11-09', tz='UTC'), 'espn schedule')
        self.assertIsNone(out[0]['competition'])


class FormTest(unittest.TestCase):
    def test_v3_form_holds_the_three_real_friendlies(self):
        used = {(s, d, h, a) for s in ('home', 'away') for d, h, a, c in form_keys(s, tr.V3_VERSION)
                if tr.is_friendly(c)}
        self.assertEqual(used, REAL_FRIENDLIES)

    def test_v4_leaves_friendlies_out_and_keeps_every_competitive_game(self):
        for side in ('home', 'away'):
            before, after = form_keys(side, tr.V3_VERSION), form_keys(side, tr.VERSION)
            self.assertEqual(len(after), 10)
            self.assertFalse(any(tr.is_friendly(c) for *_, c in after))
            # Every league, cup and European game of the v3 form is still there, in the same order.
            competitive = [k for k in before if not tr.is_friendly(k[3])]
            self.assertEqual(after[:len(competitive)], competitive)
            # The form reaches back to replace each friendly with an earlier competitive game.
            self.assertEqual(len(after) - len(competitive), len(before) - len(competitive))
            self.assertTrue(all(k[0] < competitive[-1][0] for k in after[len(competitive):]))
        self.assertEqual(form_keys('home', tr.VERSION)[-1][:3], ('2026-09-12', 'TSG Hoffenheim', 'VfB Stuttgart'))

    def test_cup_and_european_games_still_count(self):
        after = form_keys('home', tr.VERSION) + form_keys('away', tr.VERSION)
        self.assertIn(('2026-10-22', 'TSG Hoffenheim', 'Lyon', 'uefa.europa'), after)
        self.assertIn(('2026-10-28', 'Dynamo Dresden', 'Schalke 04', 'ger.dfb_pokal'), after)

    def test_rows_without_a_competition_are_kept(self):
        # Training history and Understat rows carry no competition; neither do ESPN rows frozen before v4.
        bare = evidence(labelled=False)
        self.assertEqual(eh._used_rows(tr.research_inputs(row()), bare, CUTOFF, 'home', tr.VERSION),
                         eh._used_rows(tr.research_inputs(row()), bare, CUTOFF, 'home', tr.V3_VERSION))


class PrepareTest(unittest.TestCase):
    def test_frozen_v1_forecast_replays_exactly(self):
        self.assertEqual(FIXTURE['frozen']['version'], tr.LEGACY_VERSION)
        for labelled in (False, True):  # the competition field never reaches a pre-v4 version's numbers
            again = tr.prepare(row(), CUTOFF, evidence(labelled), version=tr.LEGACY_VERSION)
            self.assertEqual(again['goal_rates'], FIXTURE['frozen']['goal_rates'])
            for key, value in FIXTURE['frozen']['margin_distribution'].items():
                self.assertAlmostEqual(again['margin_distribution'][key], value, places=15)

    def test_v1_to_v3_ignore_the_competition(self):
        for version in (tr.LEGACY_VERSION, tr.V2_VERSION, tr.V3_VERSION):
            a = tr.prepare(row(), CUTOFF, evidence(False), version=version)
            b = tr.prepare(row(), CUTOFF, evidence(True), version=version)
            self.assertEqual((a['form'], a['goal_rates'], a['margin_distribution']),
                             (b['form'], b['goal_rates'], b['margin_distribution']), version)
            self.assertNotIn('form_friendlies_excluded', b)

    def test_v4_moves_this_forecast_and_records_what_it_left_out(self):
        before = tr.prepare(row(), CUTOFF, evidence(), version=tr.V3_VERSION)
        after = tr.prepare(row(), CUTOFF, evidence())
        self.assertEqual(after['version'], 'team-form-research-v4')
        self.assertNotEqual(after['goal_rates'], before['goal_rates'])
        self.assertGreater(max(abs(a - b) for a, b in zip(hda(after), hda(before))), .001)
        # Friendlies before the cutoff, in or beyond the last ten (Hoffenheim 3, Schalke 4).
        self.assertEqual(after['form_friendlies_excluded'], {'home': 3, 'away': 4})
        self.assertEqual(after['form']['home']['all']['results'], 'DLWWWLLLLW')  # Elversberg friendly skipped; reaches back to Stuttgart (12 Sep)

    def test_v4_without_competition_labels_is_v3(self):
        # A frozen v1-v3 forecast has no labels: v4 on its own inputs changes nothing.
        new = tr.prepare(row(), CUTOFF, evidence(False))
        old = tr.prepare(row(), CUTOFF, evidence(False), version=tr.V3_VERSION)
        self.assertEqual({k: v for k, v in new.items() if k != 'version'}, {k: v for k, v in old.items() if k != 'version'})

    def test_new_forecasts_are_stamped_v4(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = tr.enrich(pd.DataFrame([row()]), tmp, fetch=False, clock=lambda: CUTOFF.to_pydatetime())
        self.assertEqual(json.loads(out.iloc[0]['team_research_json'])['version'], tr.VERSION)


if __name__ == '__main__':
    unittest.main()
