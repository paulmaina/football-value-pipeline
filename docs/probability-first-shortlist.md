# Probability-first shortlist

Policy `72h-top-ten-adjusted-probability-v12` selects the ten distinct upcoming
fixtures with the highest available reliability-adjusted probabilities, across
all requested leagues. Each fixture contributes its best-ranked usable market:
home win, away win, Over 1.5, Under 3.5, BTTS Yes, or double chance 1X/X2/12.
Quoted decimal odds break probability ties; strict qualification does not take
priority over a higher-ranked selection. Probabilities and model fitting are unchanged.

The window is anchored to generation time and ends 72 hours later. The existing
20-minute minimum kickoff lead, allowed-bookmaker policy, valid team mappings,
real exact-market quotes and reference-market freshness/integrity checks still
apply. One fixture is counted once even when duplicate provider IDs are present.
If fewer than ten distinct fixtures have usable data, the summary records the
available count and an explicit shortfall. Missing prices, duplicate fixtures or
out-of-window matches are never manufactured to reach ten.

The old probability, adjusted EV, raw EV and historical-audit thresholds now
annotate qualification rather than eliminate otherwise usable candidates.
`STRICT` means the selected market also passes those reference rules.
`PROVISIONAL` means one or more rules failed; the readable report shows the
selection warnings. A high chance of winning does not imply good value: a
selection can have negative estimated EV. None of these labels establishes
accuracy or profitability, and ten selections do not establish accumulator safety.

For Under 3.5 the reference probability thresholds are 80% blended/adjusted and
75% raw; failed historical validation remains a warning. Ranking uses the existing
development calibration adjustment where available. Unassessed calibration is
disclosed; invalid calibration data is rejected. No thresholds are changed to
make the underlying model report higher probabilities.

The prediction command is unchanged. The stored-data refresh command is also
unchanged: `py refresh_conservative_shortlist.py --root football_output_v2`.
Refreshing ranks the saved forecasts and prices; it does not fetch new odds.

Historical v9–v11 shortlists and their policy experiments replay with their
original rules. The new policy comparison captures v12 decisions explicitly.
EV sensitivity v2 compares the probability-first control (labelled `No EV gate`)
with +1.5%, +3% and +5% EV-filtered alternatives. Older experiment captures retain
their original grids and versions. Frozen predictions, selections and prices are
not rewritten when the policy changes.
