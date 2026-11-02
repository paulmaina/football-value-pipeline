"""The production allowlist must name books exactly as The Odds API titles them."""
import json
from pathlib import Path
import unittest

import quote_policy
from asian_handicap import bookmaker

ROOT = Path(__file__).resolve().parents[1]


class ProductionAllowlistTests(unittest.TestCase):
    def setUp(self):
        self.config = json.loads((ROOT/'shortlist_quote_policy.json').read_text(encoding='utf-8-sig'))

    def test_allowlist_is_pinnacle_and_1xbet_only(self):
        self.assertEqual(self.config['allowed_bookmakers'], ['Pinnacle', '1xBet'])
        self.assertEqual(self.config['fallback_bookmakers'], [])

    def test_names_match_provider_titles_exactly(self):
        titles = set(quote_policy.ODDS_API_TITLES.values())
        for name in self.config['allowed_bookmakers']:
            self.assertIn(name, titles)

    def test_bet365_is_not_allowed(self):
        policy = quote_policy.validate_policy(self.config)
        self.assertFalse(quote_policy.usable_bookmaker('bet365', policy))
        self.assertTrue(quote_policy.usable_bookmaker('1xBet', policy))
        self.assertTrue(quote_policy.usable_bookmaker('Pinnacle', policy))

    def test_provider_payload_titles_resolve(self):
        # Shape of a real EU event-odds response: key plus display title.
        payload = [{'key': key, 'title': title} for key, title in quote_policy.ODDS_API_TITLES.items()]
        policy = quote_policy.validate_policy(self.config)
        for book in payload:
            self.assertTrue(quote_policy.usable_bookmaker(book['title'], policy))
            self.assertEqual(bookmaker(book['title']), book['title'])


if __name__ == '__main__':
    unittest.main()
