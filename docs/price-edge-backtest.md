# Asian handicap price-edge backtest (pre-registered rule)

`price_edge_backtest.py` is a read-only historical test of one rule fixed before
the data was looked at: bet the Asian handicap side whose offered price beats
Pinnacle's margin-free opening price by at least 2%. It changes no production
model, policy, threshold or workflow and is not wired into any scheduled job.
Nothing in its output is a recommendation to change production.

```powershell
py price_edge_backtest.py                       # all 8 divisions, 2000 bootstrap draws
py price_edge_backtest.py --commission 0.02     # Betfair Exchange at a different rate
py price_edge_backtest.py --divisions E0 --bootstrap 300   # quick check
```

Outputs go to `football_output_v2/performance/price_edge_backtest/`:
`report.md` (verdict and tables), `summary.json` (every metric and the drop
counts) and `bets.csv` (every bet the 2% rule places, per source).

Settlement, margin removal, data loading and the gameweek block bootstrap are
reused from `ah_close_backtest.py`; see [ah-close-backtest.md](ah-close-backtest.md).

## The rule (pre-registered, not tuned)

- **Data:** football-data.co.uk CSVs in `.football_cache`, E0 SP1 D1 I1 F1 N1
  P1 T1, every season present. 2026/27 has no Pinnacle AH columns, so all of
  its matches are dropped as `no_pinnacle_open`.
- **Line:** the opening main line `AHh` (home handicap).
- **Fair probability:** Pinnacle opening `PAHH`/`PAHA`, margin removed
  proportionally. Shin is reported as a check: Shin on both the selection and
  the closing reference.
- **Bet** a side when `offered odds x fair p - 1 >= 2%`. At most one side per
  match: when both sides clear 2% (possible only at an offered overround of
  exactly 0.98), the larger edge is taken, home on a tie. A 1e-9 tolerance
  absorbs floating-point rounding so that an edge of exactly 2.0% bets.
- **Offered price sources**, each reported separately:

  | source | columns | notes |
  |---|---|---|
  | `max` | `MaxAHH`/`MaxAHA` | best across bookmakers; which bookmaker is not recorded |
  | `b365` | `B365AHH`/`B365AHA` | Bet365 |
  | `bfe` | `BFEAHH`/`BFEAHA` | Betfair Exchange, 2024/25 onwards only |
  | `avg` | `AvgAHH`/`AvgAHA` | market average; the control, which should not show an edge |

- **Commission (bfe):** 5% of net winnings by default (`--commission`). The edge
  test, the CLV and the settlement all use net odds `1 + (odds - 1) x (1 - rate)`.
  The data-quality filters check the raw quoted prices.
- **Stake and settlement:** 1 unit flat at the offered (net) odds on `AHh`.
  Quarter lines stake half on each adjacent line.

## Data-quality filters

Applied per source, in this order. A match is counted once, under the first
filter it fails, and the counts are in the report.

1. `no_pinnacle_open`: no valid `AHh` or missing `PAHH`/`PAHA`.
2. `no_pinnacle_close`: no valid `AHCh` or missing `PCAHH`/`PCAHA`.
3. `pinnacle_close_overround`: `1/PCAHH + 1/PCAHA` outside [1.00, 1.10].
4. `no_offered_price`: the source has no price for this match.
5. `offered_overround`: `1/home + 1/away < 0.98` on the offered pair.
6. `offered_above_pinnacle_cap`: either offered side is above 1.15 x
   Pinnacle's opening price on the same side. The whole pair is distrusted,
   not just the side that breaches.

Every 2025/26 league file contains rows with `MaxAHA = 22.0` (for example
Brentford v Burnley, 29/11/2025, Pinnacle 1.85). The average column is
corrupted on the same rows (`AvgAHA` around 4.3). Filter 5 drops them, and a
test pins this.

## Metrics

- **Primary:** mean CLV = offered odds x Pinnacle fair closing probability - 1,
  only where `AHCh == AHh`, with a 95% interval from resampling whole
  gameweeks (Tuesday to Monday, all leagues together); plus the share of
  those bets with CLV > 0.
- **Secondary:** ROI per unit staked with a gameweek block-bootstrap interval,
  maximum drawdown in units (the start counts as a peak) and the longest run
  of losing bets (a push or win ends a run). These include bets whose line
  moved.
- **Sensitivity only, not the rule:** thresholds 0%, 1% and 3%.
- **Breakdowns at 2%:** season, league, line type (half/quarter/whole), odds
  band (net odds), and favourite/underdog/level side. 2025/26 is also reported
  on its own as the most recent period.
- The verdict only calls an interval when it has at least 30 same-line bets.
  Smaller samples are shown in the tables but called "too few to read".

## Results (run on the cache as of 2026-11-02)

| source | bets | same-line bets | mean CLV [95%] | CLV > 0 | ROI [95%] |
|---|---|---|---|---|---|
| max | 450 | 256 | +2.46% [+1.78%, +3.17%] | 70% | +10.6% [+3.2%, +18.3%] |
| b365 | 32 | 17 | +3.16% [+1.11%, +5.03%] | 82% | +9.9% [-18.2%, +38.4%] |
| bfe | 10 | 9 | +1.15% [-3.58%, +4.20%] | 67% | -28.4% [-100%, +9.5%] |
| avg | 2 | 2 | (too few) | | |

- **Max price:** positive CLV with the interval above zero. Shin agrees
  (+2.13% [+1.43%, +2.82%]). It is positive in every season, but bet volume
  fell from 180 (2021/22) to 30 (2025/26). 2025/26 alone is +1.62%
  [-0.05%, +2.75%] over 19 same-line bets: too few to read.
- Much of the max-price CLV sits in the 2.10–2.40 odds band (+6.5% over 69
  same-line bets), and the 1.70–1.90 band is negative (-3.5% over 15).
  That pattern fits stale quotes from slow books. A backtest cannot tell a
  stale quote that was really available from a stale quote that was not.
- **Bet365, Betfair Exchange:** too few bets to say anything. Betfair
  Exchange has prices only from 2024/25.
- **Control:** the market average clears 2% only twice in five seasons, as
  expected.

## What this does and does not show

The pre-registered rule, priced at the best available bookmaker price, shows
positive closing line value with a 95% interval above zero over 2021/22 to
2025/26. History cannot show WHICH bookmaker offered the max price, whether
the price was still up when a bet could be placed, or whether the stake would
have been accepted or limited. The max-price figure is therefore an upper
bound. The real test is live tracking of prices that can actually be taken.
This backtest is not a recommendation to change production.

football-data.co.uk's "opening" prices are its collection-time snapshot
(Friday afternoon for weekend games, Tuesday for midweek), not the market's
true opening.
