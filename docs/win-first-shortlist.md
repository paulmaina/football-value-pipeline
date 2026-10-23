# Win-first shortlist (v23)

Select the strongest estimated profitable-outcome candidates from twelve distinct
matches kicking off within 48 hours. Keep the existing 20-minute pre-kickoff
buffer. Use actual, fresh Pinnacle or bet365 quotes for the exact selection.
1xBet is excluded, including when an obsolete execution configuration lists it.

For each match, rank eligible markets by the smaller of the blended and independent
model profitable-outcome probabilities, minus the development-only calibration
penalty (bounded below by zero). Then rank the match representatives globally and
take the first twelve. Adjusted EV, independent-model EV, and quoted odds resolve
probability ties; stable fixture/market/bookmaker fields resolve remaining ties.

For Asian handicaps, a profitable outcome is a full win or half win. Refunds do
not count. Their probabilities, half losses and full losses remain separately
reported. Half wins pay less than full wins; settlement-aware EV retains that
difference. Handicap win calibration is generated separately from legacy no-loss
calibration and must pass its chronological development/audit checks.

There is no fixed probability floor or EV floor. Negative adjusted EV and
negative independent-model EV appear as explicit value warnings. A high chance
of winning does not establish a good price or long-term profitability.

Identity, competition, historical reliability, probability validity, actual paired
market quotes and freshness checks remain required. The selector returns twelve
when twelve distinct matches meet those checks. It reports a shortfall instead
of inventing odds, waiving missing evidence or extending the time window.

Markets remain home win, away win, Over 1.5, the three double-chance selections,
and quoted Asian handicap lines on either team. Under 3.5 and BTTS remain excluded.

v17-v22 policies retain their definitions for archived replay. New prediction
generation and shortlist refresh use v23. Validation cache version 9 requires
the separate profitable-win evidence, so the next full prediction run rebuilds
old validation caches. Refresh alone cannot create missing win evidence or refresh
old odds; run the full prediction command after pulling the change.

Forward grading freezes the probability basis. New profitable-win probabilities
are scored against positive net settlement, with refunds scored as non-wins;
legacy handicap no-loss forecasts retain their original interpretation. Actual
settlement returns are unchanged. Twelve individual picks do not imply a reliable
twelve-leg accumulator or guaranteed winners.
