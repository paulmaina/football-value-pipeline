"""European backfill (european_backfill.py): raw files, reconciliation, reviewed names, the lock, walk-forward.

Only locked runs touch real results; nothing here reads a European holdout score.
"""
import json
from pathlib import Path
import sys
import unittest
from unittest import mock

import numpy as np
import pandas as pd

import european_backfill as eb
import european_results as er
import evaluation_harness as eh

REPO = Path(__file__).resolve().parents[1]
CACHE = REPO / '.football_cache'
CFG = json.loads((REPO / 'evaluation_harness_config.json').read_text(encoding='utf-8'))
END = CFG['european']['end_exclusive']
LOCK = pd.Timestamp(eb.LOCK_DATE)
sys.path.insert(0, str(REPO / 'scripts'))


def window(**european):
    return {**CFG, 'european': {**CFG['european'], **european}}


class RawFilesTest(unittest.TestCase):
    def test_every_raw_file_matches_its_manifest(self):
        import fetch_european_backfill as fetch
        for folder in (eb.folder(CACHE), CACHE / 'domestic_backfill'):
            manifest = json.loads((folder / 'manifest.json').read_text(encoding='utf-8'))
            self.assertTrue(manifest['files'])
            self.assertEqual(fetch.verify(folder), [], folder)
            for name, entry in manifest['files'].items():
                self.assertTrue(entry['source_url'].startswith('https://'), name)
                self.assertEqual(entry['http_status'], 200, name)
                self.assertIn('fetched_at_utc', entry)

    def test_openfootball_is_pinned_and_no_evidence_file_is_from_the_holdout_era(self):
        manifest = json.loads((eb.folder(CACHE) / 'manifest.json').read_text(encoding='utf-8'))
        for name, entry in manifest['files'].items():
            if 'openfootball' in entry['source_url']:
                self.assertRegex(entry['source_url'], r'/[0-9a-f]{40}/', name)
            self.assertNotRegex(name, r'2025|2026', name)  # 2025/26 is wholly after the European holdout start

    def test_the_live_loaders_never_read_the_backfill(self):
        # The live UCL loader reads only fdorg_history_UCL_<year>.json in the cache root, the live UEL loader only
        # europa/training.json; the backfill is in subfolders neither reads.
        self.assertFalse(list(eb.folder(CACHE).glob('fdorg_history_UCL_*.json')))
        self.assertFalse(list((CACHE / 'domestic_backfill').glob('fdorg_*')))
        self.assertEqual(len(er.load(CACHE, 'UCL', END)), 575)
        self.assertEqual(len(er.load(CACHE, 'UEL', END)), 732)


class ParserTest(unittest.TestCase):
    TEXT = '\n'.join([
        '= UEFA Champions League 2019/20', '# Matches    6', '',
        '▪ Group A', '  Tue Sep 17 2019',
        '    20:45  Club A (ESP)  v Club B (GER)  2-1 (1-0)',
        '           Club C (ITA)  v Club D (FRA)  0-0',
        '▪ Quarterfinals', '  Wed Aug 12',
        '    21:00  Club A (ESP)  v Club C (ITA)  4-2 a.e.t. (2-2, 0-2)',
        '  Thu Aug 13',
        '    21:00  Club B (GER)  v Club D (FRA)  8-7 pen. 0-0 a.e.t. (0-0)',
        '▪ Final', '  Sun Aug 23',
        '    21:00  Club A (ESP)  v Club B (GER)  3-0    [awarded]',
        '           Club C (ITA)  v Club D (FRA)  [cancelled]'])

    def test_notations_and_a_season_that_ends_in_august(self):
        rows, left_out = eb.parse_openfootball(self.TEXT, 'UCL', 2019)
        by = {(r['home'], r['away'], r['date']): r for r in rows}
        self.assertEqual(by[('Club A', 'Club B', '2019-09-17')]['regulation'], (2, 1))
        self.assertEqual(by[('Club C', 'Club D', '2019-09-17')]['regulation'], (0, 0))
        aet = by[('Club A', 'Club C', '2020-08-12')]  # Wed Aug 12 is 2020 by its weekday, not 2019
        self.assertEqual((aet['reported'], aet['regulation'], aet['duration']), ((4, 2), (2, 2), 'AET'))
        pens = by[('Club B', 'Club D', '2020-08-13')]
        self.assertEqual((pens['reported'], pens['regulation'], pens['duration']), ((0, 0), (0, 0), 'AET_PEN'))
        self.assertEqual([(r['reason'], r['reported']) for r in left_out], [('awarded', (3, 0)), ('cancelled', None)])

    def test_anything_unknown_stops_the_parse(self):
        for bad in (self.TEXT.replace('2-1 (1-0)', '2-1 aet'), self.TEXT.replace('# Matches    6', '# Matches    7'),
                    self.TEXT.replace('4-2 a.e.t. (2-2, 0-2)', '4-2 a.e.t. (2-2)'),
                    self.TEXT.replace('Wed Aug 12', 'Fri Aug 12')):  # a Friday in neither 2019 nor 2020
            with self.assertRaises(ValueError):
                eb.parse_openfootball(bad, 'UCL', 2019)


class NamesTest(unittest.TestCase):
    def test_fixture_evidence_only(self):
        left = [{'date': '2020-01-01', 'home': 'Arsenal', 'away': 'Spurs', 'reported': (2, 0)},
                {'date': '2020-02-01', 'home': 'Spurs', 'away': 'Arsenal', 'reported': (1, 1)}]
        right = [{'date': '2020-01-02', 'home': 'Arsenal FC', 'away': 'Tottenham', 'reported': (2, 0)},
                 {'date': '2020-02-01', 'home': 'Tottenham', 'away': 'Arsenal FC', 'reported': (1, 1)},
                 {'date': '2020-01-01', 'home': 'Chelsea', 'away': 'Fulham', 'reported': (2, 0)}]
        found, checked, unresolved = eb.derive_names(left, right)
        self.assertEqual(found, {'Arsenal': 'Arsenal FC', 'Spurs': 'Tottenham'})
        self.assertEqual(checked, {'Arsenal': 2, 'Spurs': 2})
        # One score differs: no mapping, however alike the names are.
        right[1] = {**right[1], 'reported': (0, 1)}
        found, _, unresolved = eb.derive_names(left, right)
        self.assertEqual(found, {})
        self.assertEqual(sorted(unresolved), ['Arsenal', 'Spurs'])
        # Two fixtures on one day with the same score cannot tell clubs apart.
        found, _, unresolved = eb.derive_names(left[:1], right[:1] + [right[2]])
        self.assertEqual(found, {})

    def test_committed_aliases_are_what_fixture_evidence_derives(self):
        self.assertEqual(eb.verify_aliases(CACHE), [])
        committed = json.loads(eb.DOMESTIC_ALIASES.read_text(encoding='utf-8'))
        self.assertEqual(committed['aliases'], eb.domestic_aliases(CACHE)['aliases'])

    def test_ucl_links_and_the_unlinked_clubs(self):
        aliases = eb.load_aliases()
        names = aliases['UCL']['to_football_data_org']
        self.assertEqual(names['Bayern München'], 'FC Bayern München')
        self.assertEqual(names['Atlético Madrid'], 'Club Atlético de Madrid')
        self.assertEqual(len(set(names.values())), len(names))  # one to one
        links = aliases['UCL']['evidence']['links']
        self.assertTrue(all(links['linked'][o] for o in names))  # each link names its bridge
        for club in ('Dinamo Zagreb', 'Olympiakos Piraeus', 'Slavia Praha', 'Qarabağ FK'):
            self.assertIn(club, links['not_linked'])  # no reviewed evidence: left apart, reported

    def test_the_nine_domestic_gaps(self):
        evidence = json.loads(eb.DOMESTIC_ALIASES.read_text(encoding='utf-8'))['evidence']
        self.assertEqual(set(evidence), set(eb.DOMESTIC_GAPS))
        added = {k for k, v in evidence.items() if v['alias']}
        self.assertEqual(added, set(eb.DOMESTIC_GAPS) - {'Galatasaray SK', 'Fenerbahçe SK'})
        self.assertEqual(evidence['SSC Napoli']['alias'], 'Napoli')
        self.assertEqual(evidence['n.e.c.']['alias'], 'Nijmegen')

    def test_domestic_aliases_apply_only_where_the_research_resolver_has_no_answer(self):
        histories = {'SerieA': (None, {'Napoli', 'Lazio'})}
        mapped, _ = er.domestic_identities(['SSC Napoli', 'Lazio', 'Galatasaray SK'], histories,
                                           {'SerieA': {'SSC Napoli': 'Napoli', 'Galatasaray SK': 'Galatasaray'}})
        self.assertEqual(mapped, {'SSC Napoli': ('SerieA', 'Napoli'), 'Lazio': ('SerieA', 'Lazio')})
        # The UEL form of the same name (the reviewed Europa key) finds it; a near miss does not.
        mapped, _ = er.domestic_identities(['ssc napoli', 'SSC Napoli 1926'], histories,
                                           {'SerieA': {'SSC Napoli': 'Napoli'}})
        self.assertEqual(mapped, {'ssc napoli': ('SerieA', 'Napoli')})


class ReconciliationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.frame, cls.report = eb.reconcile(CACHE)
        cls.by = {(r['competition'], r['season']): r for r in cls.report}

    def test_seasons_sources_agreements_and_conflicts(self):
        for key, admitted in {('UCL', '2015/16'): 125, ('UCL', '2016/17'): 125, ('UCL', '2019/20'): 119,
                              ('UCL', '2022/23'): 125, ('UEL', '2020/21'): 204, ('UEL', '2021/22'): 139}.items():
            self.assertEqual(self.by[key]['admitted'], admitted, key)
        for entry in self.report:
            if entry.get('score_conflicts') is not None:
                self.assertEqual(entry.get('score_conflicts', []), [], entry['season'])
        for season in ('2015/16', '2016/17'):
            self.assertIn('single source', self.by[('UCL', season)]['label'])
        for season in ('2017/18', '2018/19', '2019/20', '2020/21', '2021/22', '2022/23'):
            entry = self.by[('UCL', season)]
            self.assertEqual(entry['agreements'], entry['admitted'])
            self.assertEqual((entry['openfootball_only'], entry['fixture_download_only']), ([], []))
        self.assertEqual(self.by[('UEL', '2019/20')]['admitted'], 0)  # Fixture Download alone is not enough
        self.assertEqual([x['reason'] for x in self.by[('UEL', '2020/21')]['left_out_not_played']], ['awarded'])
        self.assertEqual([x['reason'] for x in self.by[('UEL', '2021/22')]['left_out_not_played']], ['cancelled'] * 2)
        self.assertEqual(len(self.frame), 994 + 343)

    def test_no_backfilled_row_reaches_the_cached_seasons(self):
        self.assertTrue((self.frame.Date < LOCK).all())
        for competition in ('UCL', 'UEL'):
            old = self.frame.loc[self.frame.competition == competition]
            self.assertLess(old.Date.max(), er.load(CACHE, competition, END).Date.min())

    def test_rows_on_or_after_the_holdout_start_and_every_cached_row_are_unchanged(self):
        for competition in ('UCL', 'UEL'):
            live = er.load(CACHE, competition, END)
            full = er.load_with_backfill(CACHE, competition, END)
            tail = full.loc[full.Date >= live.Date.min()].reset_index(drop=True)
            pd.testing.assert_frame_equal(tail, live)  # every cached row, byte for byte as live loads it
            pd.testing.assert_frame_equal(full.loc[full.Date >= LOCK].reset_index(drop=True),
                                          live.loc[live.Date >= LOCK].reset_index(drop=True))
            self.assertEqual(len(full) - len(live), int((self.frame.competition == competition).sum()))


class BackfillHarnessTest(unittest.TestCase):
    def test_development_starts_where_the_warm_up_ends(self):
        for competition, day in (('UCL', '2017-09-04'), ('UEL', '2021-10-25')):
            data = er.load_with_backfill(CACHE, competition, END)[['Date']]
            self.assertEqual(eh.check_development_start(data, competition, CFG), pd.Timestamp(day))
        with self.assertRaises(ValueError):
            eh.check_development_start(er.load_with_backfill(CACHE, 'UCL', END)[['Date']], 'UCL',
                                       window(development_start={'UCL': '2017-09-18', 'UEL': '2021-10-25'}))

    def test_the_fold_grid_is_the_one_before_the_backfill(self):
        e = CFG['european']
        before = {**e, 'test_start': '2022-08-01'}
        end = pd.Timestamp(e['end_exclusive'])
        self.assertTrue({w for w in eh.fold_windows(before, end)} <= set(eh.fold_windows(e, end)))

    def test_walk_forward_a_later_result_never_changes_an_earlier_forecast(self):
        cfg = window(end_exclusive='2018-01-01')
        data = er.load_with_backfill(CACHE, 'UCL', END)
        data = data.loc[data.Date < '2018-01-01'].copy()
        before = eh.evaluate_european('UCL', None, cfg, data=data)
        self.assertEqual(before[2]['UCL:warm_up'], 250)
        changed = data.copy()
        target = changed.index[changed.Date.dt.date.astype(str) == '2017-11-01'][0]
        changed.loc[target, ['FTHG', 'FTAG']] = [9, 0]
        after = eh.evaluate_european('UCL', None, cfg, data=changed)
        b = {r['fixture_key']: r['probs'] for r in before[3]}
        a = {r['fixture_key']: r['probs'] for r in after[3]}
        cut = '2017-11-01'
        # Every forecast up to the changed match is identical (and present in both runs); later ones may change,
        # or vanish when the changed result makes a later fold's Dixon-Coles grid invalid.
        self.assertEqual({k for k in b if k.split('|')[1] <= cut}, {k for k in a if k.split('|')[1] <= cut})
        earlier = [(b[k], a[k]) for k in b if k.split('|')[1] <= cut]
        later = [(b[k], a[k]) for k in b if k.split('|')[1] > '2017-11-13' and k in a]
        self.assertTrue(earlier and later)
        self.assertTrue(all(x == y for x, y in earlier))
        self.assertTrue(any(x != y for x, y in later))
        self.assertNotIn('warm_up', {r['phase'] for r in before[3]})  # warm-up rows train, never score

    def test_odds_are_ignored(self):
        cfg = window(end_exclusive='2017-12-01')
        data = er.load_with_backfill(CACHE, 'UCL', END)
        data = data.loc[data.Date < '2017-12-01'].copy()
        base = eh.evaluate_european('UCL', None, cfg, data=data)[3]
        rng = np.random.default_rng(5)
        priced = data.copy()
        for c in ('PSH', 'PSD', 'PSA', 'B365H', 'B365D', 'B365A', 'P>2.5', 'P<2.5', 'AHh', 'PAHH', 'PAHA', 'AvgH'):
            priced[c] = rng.uniform(1.1, 15., len(priced))
        again = eh.evaluate_european('UCL', None, cfg, data=priced)[3]
        self.assertTrue(base)
        self.assertEqual(base, again)

    def test_the_european_lock_holds_with_the_backfill(self):
        cfg = window(test_start='2025-01-06', end_exclusive='2025-03-15')
        records, _, coverage, calib = eh.european(CACHE, cfg, competitions=['UCL'])
        self.assertEqual(records, [])  # every UCL match in the window is in the locked holdout
        self.assertGreater(coverage['UCL:locked_holdout'], 0)
        data = er.load_with_backfill(CACHE, 'UCL', END)
        train = eh.european_training_rows(data, 'UCL', CFG, False)
        self.assertFalse(train.Date.map(lambda d: eh.european_phase(d, 'UCL', CFG) == 'holdout').any())

    def test_holdout_reach_reads_no_score(self):
        real = er.load_with_backfill(CACHE, 'UCL', END)
        first = eh.european_holdout_reach(CACHE, CFG)
        scrambled = real.copy()
        scrambled[['FTHG', 'FTAG']] = 99
        with mock.patch.object(er, 'load_with_backfill', return_value=scrambled):
            second = eh.european_holdout_reach(CACHE, CFG)
        self.assertEqual(first, second)
        self.assertEqual(first['UCL']['fixtures'], 288)
        self.assertEqual(first['UCL']['weeks'], 29)
        self.assertEqual(first['UCL']['declared_run_would_score'] + sum(first['UCL']['left_out'].values()), 288)


class ReviewedAliasesTest(unittest.TestCase):
    """The manual reviewed aliases (docs/audits/european-reviewed-aliases.json, Phase 2c alias review)."""
    def test_marked_manual_and_scoped_before_the_european_holdout(self):
        data = json.loads(eb.REVIEWED_ALIASES.read_text(encoding='utf-8'))
        self.assertEqual(data['status'], 'manual, approved by Paul in PR review')
        self.assertEqual(data['applies_before'], eb.LOCK_DATE)
        reviewed = eb.load_reviewed_aliases()
        self.assertEqual(reviewed['ucl_names'], {
            'Dinamo Zagreb': 'GNK Dinamo Zagreb', 'Olympiakos Piraeus': 'PAE Olympiakos SFP',
            'Slavia Praha': 'SK Slavia Praha', 'Qarabağ FK': 'Qarabağ Ağdam FK', 'AEK Athen': 'PAE AEK'})
        for table in data['domestic']['aliases'].values():
            for entry in table.values():
                self.assertTrue(entry['country'] and entry['sources'] and entry['reason'])
        # None of them is a fixture-evidence alias: each fills a gap the evidence left.
        derived = eb.load_aliases()['UCL']['to_football_data_org']
        self.assertFalse(set(reviewed['ucl_names']) & set(derived))
        evidence = eb.load_domestic_aliases()
        for league, table in reviewed['domestic'].items():
            self.assertFalse(set(table) & set(evidence.get(league, {})))

    def test_only_backfilled_rows_are_renamed_and_holdout_rows_are_byte_identical(self):
        before = er.load_with_backfill(CACHE, 'UCL', END, reviewed=False)
        after = er.load_with_backfill(CACHE, 'UCL', END)
        self.assertEqual(len(before), len(after))
        pd.testing.assert_frame_equal(after.loc[after.Date >= LOCK].reset_index(drop=True),
                                      before.loc[before.Date >= LOCK].reset_index(drop=True))
        live = er.load(CACHE, 'UCL', END)
        pd.testing.assert_frame_equal(after.loc[after.Date >= LOCK].reset_index(drop=True),
                                      live.loc[live.Date >= LOCK].reset_index(drop=True))
        changed = (before.HomeTeam != after.HomeTeam) | (before.AwayTeam != after.AwayTeam)
        self.assertTrue(changed.any())
        self.assertLess(after.loc[changed].Date.max(), pd.Timestamp('2023-07-01'))  # backfill seasons only
        names = set(after.HomeTeam) | set(after.AwayTeam)
        self.assertFalse(set(eb.load_reviewed_aliases()['ucl_names']) & names)
        uel = er.load_with_backfill(CACHE, 'UEL', END)
        pd.testing.assert_frame_equal(uel, er.load_with_backfill(CACHE, 'UEL', END, reviewed=False))

    def test_a_reviewed_alias_must_join_an_older_name_to_a_cached_one(self):
        old = pd.DataFrame({'Date': [pd.Timestamp('2019-09-17')], 'HomeTeam': ['Slavia Praha'], 'AwayTeam': ['Inter']})
        with self.assertRaises(ValueError):
            er.rename_reviewed(old, {'Inter'}, {'Slavia Praha': 'SK Slavia Praha'})  # target not cached
        with self.assertRaises(ValueError):
            er.rename_reviewed(old, {'Slavia Praha', 'SK Slavia Praha'}, {'Slavia Praha': 'SK Slavia Praha'})
        with self.assertRaises(ValueError):
            er.rename_reviewed(old.assign(Date=LOCK), {'SK Slavia Praha'}, {'Slavia Praha': 'SK Slavia Praha'})

    def test_domestic_reviewed_aliases_apply_only_before_the_european_holdout(self):
        frame = pd.DataFrame({'Date': pd.date_range('2023-08-01', periods=40, freq='7D'),
                              'HomeTeam': ['Galatasaray', 'Besiktas'] * 20, 'AwayTeam': ['Besiktas', 'Galatasaray'] * 20})
        histories = {'SuperLig': (frame, {'Galatasaray', 'Besiktas'})}
        fixtures = pd.DataFrame({'Date': [pd.Timestamp('2024-06-01'), pd.Timestamp('2025-02-01')],
                                 'HomeTeam': ['Galatasaray SK'] * 2, 'AwayTeam': ['Besiktas'] * 2})
        flags, _ = er.domestic_form_coverage(fixtures, histories, reviewed={'SuperLig': {'Galatasaray SK': 'Galatasaray'}},
                                             reviewed_before=eb.LOCK_DATE)
        self.assertEqual(flags.home_league.iat[0], 'SuperLig')
        self.assertTrue(pd.isna(flags.home_league.iat[1]))
        self.assertGreater(flags.home_domestic_matches.iat[0], 0)
        self.assertEqual(flags.home_domestic_matches.iat[1], 0)
        with self.assertRaises(ValueError):  # never overrides a fixture-evidence alias
            er.merge_aliases({'SerieA': {'SSC Napoli': 'Napoli'}}, {'SerieA': {'SSC Napoli': 'Lazio'}})


class DomesticBackfillTest(unittest.TestCase):
    def test_domestic_backfill_loads_and_stays_out_of_the_domestic_harness(self):
        rule = CFG['european']['domestic_form']
        import historical_benchmark as hb
        for league in CFG['leagues']:
            data, dropped = er.load_domestic_backfill(CACHE / rule['backfill_folder'], hb.CODES[league],
                                                      rule['backfill_seasons'])
            self.assertLess(data.Date.max(), pd.Timestamp('2021-07-01'))
            self.assertGreater(data.Date.min(), pd.Timestamp('2015-07-01'))
            self.assertEqual(dropped.get('unfinished_rows', 0), 0)
        # The domestic harness: same seasons, and its setup fingerprint never hashes a backfill file.
        self.assertEqual(CFG['seasons'][0], '2122')
        parts = eh.setup_fingerprint(CFG, CACHE)['parts']
        self.assertFalse([p for p in parts if 'backfill' in p])


if __name__ == '__main__':
    unittest.main()
