# Asian handicap price edge vs Pinnacle (v28)

**Generated (UTC):** 2026-11-04T10:20:33.895771+00:00. **Picks:** 1 (one per match, no cap, safest first). **Status:** BELOW_TARGET.
**Rule:** edge = price x Pinnacle fair win-share - 1, at least 2.0% against Pinnacle (a: same AH line, b: equivalent market) or 3.0% against the derived market-implied price (c: plus lines only). Odds above 3.00, prices above 1.15 x fair, quotes more than 10 minutes apart and Pinnacle overrounds outside [1.00, 1.10] are rejected.
**Tags** (balanced, low total, high draw, even odds) are tracked hypotheses only; they never change a pick.
**Cagey correction (v28):** derived plus lines (+1 or more) are priced from the cagey-corrected matrix (c-cagey). Picks that qualified only because of the correction: 0.
**Model vs Pinnacle gap** is information only; the model does not select picks.

> A price edge is not a guaranteed profit. Grade it by closing line value against the Pinnacle close.

## Picks

| Kickoff (UTC) | League | Home | Away | Balanced | Low total | High draw | Even odds | Pinnacle draw probability | Pinnacle P(over 2.5) | AH line | Side | Favourite/underdog | Market to bet | Bookmaker | Price | Fair odds | Reference | Edge | Minimum odds still worth taking | Pinnacle no-loss probability | Offered quote age (min) | Pinnacle quote age (min) | Model vs Pinnacle gap (info only) | Cagey score: P(2+ goal margin) (info only) | Cagey fit | Fair (uncorrected) | Qualified only because of correction | Corrected cagey score | Other value lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-11-04T20:00:00+00:00 | UEFA Champions League | PSV Eindhoven | Club Brugge | False | False | False | False | 22.0% | 68.8% | +0.00 | home | favourite | Asian Handicap Home +0.00 | 1xBet | 1.58 | 1.54 | b: Pinnacle equivalent market | +2.8% | 1.57 | 72.7% | 1 | 0 | -0.5% | 42.6% | B | 1.54 | False | 43.5% | Home win @ 1xBet 2.02 (+2.8%) |

## Rejections by reason

| Reason | Candidates |
| --- | --- |
| edge below 2% | 862 |
| offered odds above 3.00 | 186 |
| kickoff outside 20-minute to 48-hour window | 130 |
| no offered quote at an allowed bookmaker | 115 |
| no Pinnacle reference | 84 |
| edge below 3% | 24 |
| Pinnacle overround outside [1.00, 1.10] | 14 |
| offered price above 1.15 x fair odds | 2 |

Tagged candidates: {'balanced': 289, 'low_total': 0, 'high_draw': 36, 'even_odds': 18}.

## Cagey tier (separate list, never merged with the picks above)

Every match with P(narrow: draw or 1-goal win) >= 63% in the 20-minute to 48-hour window, with its safest AH +1 to +2.25 line at Pinnacle or 1xBet after the data-quality checks; one per match, safest first. **Price vs fair** says whether the price gives expected profit >= 0 after stake cost under the corrected matrix (value) or not (below fair). This run: 7 matches, 1 value, 6 below fair.

| Kickoff (UTC) | League | Home | Away | Balanced | Low total | High draw | Even odds | Pinnacle draw probability | Pinnacle P(over 2.5) | AH line | Side | Favourite/underdog | Market to bet | Bookmaker | Price | Fair odds | Reference | Edge | Minimum odds still worth taking | Pinnacle no-loss probability | Offered quote age (min) | Pinnacle quote age (min) | Model vs Pinnacle gap (info only) | Cagey score: P(2+ goal margin) (info only) | Cagey fit | Fair (uncorrected) | Qualified only because of correction | Corrected cagey score | P(narrow: draw or 1-goal win) | P(draw) | P(1-goal win) | P(margin 3+) | Out of training domain | Corrected no-loss probability | Full win | Half win | Push | Half loss | Full loss | Profit probability | Corrected fair odds | Uncorrected fair odds | Expected profit | Price vs fair (value / below fair) | Pinnacle fair odds (if quoted) | Also in value tier |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-11-04T20:00:00+00:00 | UEFA Champions League | Porto | Napoli | False | False | False | False | 0.24932458510227712 | 0.5626598465473145 | 1.0 | home | favourite | Asian Handicap Home +1.00 | 1xBet | 1.07 | 1.1136478360629778 | c-cagey | -0.039193571477033284 | 1.1470572711448672 | 0.9071693582042785 | 3.34826285 | 0.4815961833333333 | 0.008245463434036204 | 0.3886662178011221 | B | 1.1207802580727555 | False | 36.8% | 63.2% | 25.7% | 37.5% | 15.9% | yes | 91.3% | 76.9% | 0.0% | 14.3% | 0.0% | 8.7% | 76.9% | 1.11 | 1.12 | -3.4% | below fair | — | False |
| 2026-11-05T20:00:00+00:00 | UEFA Europa League | Celta Vigo | Union Saint-Gilloise | True | False | False | False | 0.2623831463036953 | 0.5511811023622047 | 1.0 | away | underdog | Asian Handicap Away +1.00 | Pinnacle | 1.32 | 1.3952095808383236 | a | -0.053905579399141645 | 1.4231137724550902 | 0.7817448226649027 | 0.4315961833333333 | 0.4315961833333333 | 0.07116950185178506 | 0.3582478817399389 | B | 1.3952095808383236 | False | 34.5% | 65.5% | 26.7% | 38.7% | 13.0% | yes | 79.0% | 57.8% | 0.0% | 21.1% | 0.0% | 21.0% | 57.8% | 1.36 | 1.38 | -2.5% | below fair | 1.40 | False |
| 2026-11-04T15:30:00+00:00 | UEFA Europa League | Rennes | Olympiakos Piraeus | True | False | False | False | 0.2694740272243864 | 0.5424164524421594 | 1.0 | away | underdog | Asian Handicap Away +1.00 | Pinnacle | 1.34 | 1.3906705539358601 | a | -0.036436058700209606 | 1.4184839650145773 | 0.7773809157463417 | 0.4315961833333333 | 0.4315961833333333 | -0.06852526381143553 | 0.3563201059976842 | B | 1.3906705539358601 | False | 34.2% | 65.8% | 27.5% | 38.3% | 12.9% | yes | 78.7% | 57.5% | 0.0% | 21.2% | 0.0% | 21.3% | 57.5% | 1.37 | 1.39 | -1.8% | below fair | 1.39 | False |
| 2026-11-05T20:00:00+00:00 | UEFA Europa League | AZ Alkmaar | Juventus | False | False | False | False | 0.2550898978604992 | 0.5326370757180157 | 1.5 | home | underdog | Asian Handicap Home +1.50 | Pinnacle | 1.28 | 1.3386243386243388 | a | -0.0437944664031622 | 1.3653968253968256 | 0.7478648253535835 | 0.4315961833333333 | 0.4315961833333333 | -0.08730297052519553 | 0.3621645588709067 | B | 1.3386243386243388 | False | 33.9% | 66.1% | 26.4% | 39.7% | 13.3% | yes | 76.4% | 76.4% | 0.0% | 0.0% | 0.0% | 23.6% | 76.4% | 1.31 | 1.34 | -2.2% | below fair | 1.34 | False |
| 2026-11-05T20:00:00+00:00 | UEFA Europa League | Hapoel Be'er Sheva | OFI Crete | True | False | False | False | 0.26084486963881987 | 0.5692307692307692 | 1.0 | away | underdog | Asian Handicap Away +1.00 | Pinnacle | 1.38 | 1.4451612903225803 | a | -0.04508928571428561 | 1.474064516129032 | 0.7558421039524208 | 0.4315961833333333 | 0.4315961833333333 | 0.1885081561268619 | 0.37071966665011685 | B | 1.4451612903225803 | False | 35.9% | 64.1% | 26.5% | 37.5% | 14.4% | yes | 76.3% | 55.0% | 0.0% | 21.3% | 0.0% | 23.7% | 55.0% | 1.43 | 1.45 | -2.8% | below fair | 1.45 | False |
| 2026-11-05T17:45:00+00:00 | UEFA Europa League | PFC Levski Sofia | Jagiellonia Białystok | False | False | False | False | 0.268854398487969 | 0.5259067357512953 | 1.0 | away | underdog | Asian Handicap Away +1.00 | Pinnacle | 1.42 | 1.4813559322033898 | a | -0.041418764302059485 | 1.5109830508474575 | 0.74516327794301 | 0.4315961833333333 | 0.4315961833333333 | -0.19372483023978188 | 0.3611659088706861 | B | 1.4813559322033898 | False | 33.8% | 66.2% | 27.8% | 38.4% | 13.3% | yes | 76.1% | 53.4% | 0.0% | 22.7% | 0.0% | 23.9% | 53.4% | 1.45 | 1.48 | -1.5% | below fair | 1.48 | False |
| 2026-11-05T20:00:00+00:00 | UEFA Europa League | Torreense | FC Ararat-Armenia | False | False | False | False | 0.24317309321288952 | 0.47409326424870474 | 1.0 | away | underdog | Asian Handicap Away +1.00 | Pinnacle | 1.58 | 1.6475409836065575 | a | -0.04099502487562201 | 1.6804918032786886 | 0.7137858443866755 | 0.4315961833333333 | 0.4315961833333333 | -0.18146878126695692 | 0.3611388137280588 | B | 1.6475409836065575 | False | 31.8% | 68.2% | 25.8% | 42.4% | 12.4% | yes | 74.8% | 48.0% | 0.0% | 26.7% | 0.0% | 25.2% | 48.0% | 1.53 | 1.62 | +2.6% | value | 1.65 | False |
