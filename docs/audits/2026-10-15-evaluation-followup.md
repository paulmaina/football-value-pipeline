# Claude evaluation follow-up — 15 October 2026

## Applicable corrections

Reproduced the evaluation's six direct-pytest subtest failures in the
all-market threshold test with the user's 1xBet-only policy present. These
were test-fixture/configuration failures, not evidence that valid production
1xBet quotes were being rejected. The canonical `run_offline_tests.py` already
injected an offline policy, explaining why CI passed while direct runs failed.

All unittest cases now inherit a test-scoped policy guard. The guard surrounds
the test lifecycle, including custom setup/teardown and failures, restores the
previous setting, and never modifies the production JSON file. Explicit policy
tests can still override it. The tests package also supports the existing
sibling fixture imports under dotted unittest names. CI now exercises ordinary
pytest in addition to the canonical coverage runner and a dotted unittest
smoke check. Pytest is a development dependency only.

Supported commands, with `shortlist_quote_policy.json` still present:

```powershell
py run_offline_tests.py
py -m pytest -q tests
py -m unittest discover -s tests -q
py -m unittest tests.test_all_market_ev_thresholds tests.test_double_chance
```

Validation: the canonical coverage runner and ordinary unittest discovery each
pass all 300 tests. Ordinary pytest passes 307 collected cases and 39 subtests;
the framework counts differ, not the evidence. Both deliberate failed-fit
warnings are confined to the failure-isolation regression. Coverage floors and
the 76-module/13-CLI smoke checks pass. The production policy remains present
and its bytes are unchanged throughout testing.

## Model findings and decisions

| Finding | Current implementation / evidence | Action |
|---|---|---|
| L2=3 improves retrospective goal scores but worsens blended audit 1X2 slightly | Existing reliability trial changes L2 alone against actual production forecasts. Both development and audit periods have already been inspected. | Keep the registered trial and its guardrails; do not replace the shared production model based on goal-market scores alone. |
| Pinnacle totals anchoring improves retrospective goal scores | Existing totals-anchor trial already tests this against production; unavailable inputs stay unavailable. | Continue the same forward trial. No additional sidecar or automatic promotion. |
| A market weight of 0.85 approaches closing-reference 1X2 scores | Existing benchmark forward trial already tests the nominated weight; an opening/closing timing difference remains in the historical comparison. | Use the existing paired forward evidence. Forecast accuracy near the market does not establish executable betting value. |
| Production half-life is described as 240 days | 240 is the default and the fixed historical benchmark's reference. The normal command uses `--tune-half-life`, which selects league-specific values. | Assess the baseline using archived per-run diagnostics, not the default value alone. |
| Positive CLV evidence is absent | At checked main commit 4dd7e442cfbcd71bb2892e60e3a75f2fa178fd8e, the report contains seven observations but no covered 1xBet selections; one Pinnacle selection has coverage. | Continue the existing collector and inspect coverage. A local scheduled task requires the user's awake Windows environment; offline testing cannot establish live coverage. |
| New information such as xG, lineups or rest days may help | No timestamped historical source or independent improvement evidence was supplied in this evaluation. | Defer additions, preserving the agreed fixed experiment set. |

The checked forward summaries contain **zero paired settled fixtures** for
the L2/half-life candidates, totals anchoring and market-weight trial. They
therefore do not justify a production parameter change today. The historical
benchmark and Claude's analysis reuse the same data; they are corroborating
retrospective diagnostics, not independent prospective confirmation.

The subjective 5.5/10 rating is not a model-selection metric. Use paired
probability losses, calibration, coverage, uncertainty and real quote evidence
under the existing registered gates. Passing the corrected software tests
improves evaluation reliability; it does not itself prove better forecasts,
positive CLV or profitability. No model, shortlist threshold, bookmaker
allowlist or production prediction output is changed by this patch.
