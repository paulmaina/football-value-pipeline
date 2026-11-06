"""All captured pre-kickoff recommendations, distinct from latest picks or placed bets."""
import hashlib
import json
import pandas as pd


def rows(root, archive):
    from performance_tracking import frozen_rows, fixture_key, utc
    from price_edge_tracking import archived_tier_rows, POLICIES
    value = [r for r in frozen_rows(archive,'shortlist',all_runs=True) if r.get('selection_policy_version') in POLICIES]
    cagey = archived_tier_rows(root,archive)
    output = {}; order = lambda r: str(r.get('snapshot_captured_utc') or '')
    for source, records in (('value',value),('cagey',cagey)):
        for row in sorted(records,key=order):
            # Prices/lines normalize CSV numeric spelling; re-uploading a run is not a new recommendation.
            def numeric(key):
                value = pd.to_numeric(row.get(key),errors='coerce')
                return float(value) if pd.notna(value) else None
            stamp = utc(row.get('snapshot_generated_utc'))
            identity = [source,stamp.isoformat(),fixture_key(row),str(row.get('market') or ''),
                        row.get('handicap_side'),numeric('handicap_line'),str(row.get('bookmaker') or ''),
                        numeric('offered_decimal_odds')]
            identifier = hashlib.sha256(json.dumps(identity,separators=(',',':')).encode()).hexdigest()[:24]
            output.setdefault(identifier,{**row,'recommendation_id':identifier,'recommendation_tier':source,
                                          'evaluation_view':'all_captured_generations'})
    return list(output.values())


def summarize(frame):
    from performance_tracking import fixture_key
    result = {}
    for source in ('value','cagey'):
        part = frame.loc[frame.recommendation_tier.eq(source)] if len(frame) else frame
        profit = pd.to_numeric(part.get('unit_profit',pd.Series(dtype=float)),errors='coerce').dropna()
        result[source] = dict(recommendations=len(part),graded=len(profit),
            distinct_fixtures=int(part.apply(fixture_key,axis=1).nunique()) if len(part) else 0,
            simulated_mean_unit_return=float(profit.mean()) if len(profit) else None,
            positive_return_share=float((profit>0).mean()) if len(profit) else None,
            no_loss_share=float((profit>=0).mean()) if len(profit) else None)
    result['note'] = ('Every captured generation is graded at its own offered odds; re-uploads deduplicate. '
                      'Repeated fixtures and overlapping lists are correlated recommendations, not independent '
                      'bets. Unit returns are hypothetical, not actual betting ROI. Latest-view reports remain separate.')
    return result
