# Conservative shortlist policy v4: double chance

Policy `72h-double-chance-v4` excludes Under 3.5 from future STRICT and PROVISIONAL shortlists and adds **Double Chance 1X** (home or draw) and **Double Chance X2** (draw or away). Home win, away win, Over 1.5 and BTTS Yes remain supported. The 12 double-chance market is not selected. Existing archived Under 3.5 picks remain graded normally. General Under 3.5 predictions, validation and the shadow experiment are retained.

1X probabilities are home+draw; X2 probabilities are draw+away, calculated separately for raw DC and the existing 1X2-reweighted model. This does not create an offered price. Exact double-chance quotes are requested in the existing bounded event-odds requests using `double_chance`. The request-count cap is unchanged, but adding a market can increase provider credit usage per request. The cache namespace changes so old responses without double chance are not reused.

Provider documentation:
- https://the-odds-api.com/sports/epl-odds.html (documented outcome labels such as `Chelsea or Draw`)
- https://the-odds-api.com/sports-odds-data/betting-markets.html

A usable bookmaker response must contain all three overlapping outcomes from the same bookmaker. Margin removal proportionally normalizes inverse prices to **two**, because each 1X2 result occurs in two double chances. It does not normalize these overlapping outcomes as three mutually exclusive probabilities. References with impossible implied probabilities or sum outside 1.96–2.40 are rejected. Best quoted prices are used for EV; prices are never synthesized from 1X2 odds. Unknown labels and incomplete books are unavailable.

Double chance is STRICT-only in v4. Requirements include model probability >=80%, raw probability >=75%, at least two bookmakers, a valid fresh reference and quoted price, existing identity/kickoff requirements, at least +3% calibration-adjusted estimated EV, nonnegative raw EV, and passing chronological market/high-confidence reliability gates. These thresholds are conservative starting rules, not empirically proven optimal or a guarantee of profit. Missing validation fails closed even when the generic filter is called without reports. Historical probability validation comes from chronological 1X2 forecasts and observed results; no historical double-chance betting ROI is claimed without actual quoted historical prices. Cached validation is invalidated by validator version 4.

Settlement uses regulation-time results: home goals >= away goals wins 1X; away goals >= home goals wins X2. A draw wins both. The normal performance report and Excel market/policy breakdowns include the new selections. Archived forecasts and policies are not rewritten.

## Use

```powershell
git pull --rebase origin main
py football_value_pipeline_v2_standalone.py --leagues EPL LaLiga Bundesliga SerieA Ligue1 UCL --tune-half-life --goal-blend-experiment
py format_football_output.py
```

The first run rebuilds historical validation and fetches eligible event markets. Fewer selections, including no double-chance selections, is valid when coverage or qualification is inadequate. Commit/push raw and readable outputs before kickoff as usual. Existing generated files do not change merely by updating code: rerun the pipeline for fresh odds, or `py refresh_conservative_shortlist.py` to remove excluded markets using stored data (no new quotes/refitting).

No policy can produce a perfect shortlist. This change does not resolve upstream training-data gaps; verify training dates separately. Continue forward testing, and compare the new policy separately from the earlier Under 3.5 policy.
