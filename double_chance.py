"""Regulation-time double chance; real quotes only, never synthetic prices."""
import math

MARKETS = {'home_draw': 'Double Chance 1X', 'draw_away': 'Double Chance X2'}


def probabilities(pred):
    out = {}
    for prefix in ('p_', 'raw_p_'):
        try:
            h,d,a = [float(pred[prefix+k]) for k in ('home','draw','away')]
        except (KeyError,TypeError,ValueError):
            continue
        if not all(math.isfinite(v) and 0 <= v <= 1 for v in (h,d,a)) or abs(h+d+a-1) > 1e-6:
            continue
        out[prefix+'home_draw'] = min(1.,h+d)
        out[prefix+'draw_away'] = min(1.,d+a)
    return out


def parse_quotes(payload):
    """Normalize a complete overlapping DC book to total probability two.

    Each underlying 1X2 outcome belongs to two double chances. Dividing a DC
    triple by its sum as if it were mutually exclusive would be incorrect.
    Proportional margin removal is a reference estimate, not a calibrated model.
    """
    home,away = payload.get('home_team'),payload.get('away_team')
    if not isinstance(home,str) or not isinstance(away,str) or home==away:
        return {}
    labels={}
    for key,left,right,short in [('home_draw',home,'Draw','1X'),
                                ('draw_away',away,'Draw','X2'),
                                ('home_away',home,away,'12')]:
        for name in (f'{left} or {right}',f'{right} or {left}',
                     f'{left}/{right}',f'{right}/{left}',short):
            labels[name.casefold()] = key
    offers=[]
    books=payload.get('bookmakers')
    if not isinstance(books,list): return {}
    for book in books:
        if not isinstance(book,dict): continue
        name=book.get('title') or book.get('key')
        if not isinstance(name,str) or not name.strip(): continue
        markets=book.get('markets')
        if not isinstance(markets,list): continue
        for market in markets:
            if not isinstance(market,dict) or market.get('key')!='double_chance': continue
            prices={};duplicate=False
            outcomes=market.get('outcomes')
            if not isinstance(outcomes,list): continue
            for outcome in outcomes:
                if not isinstance(outcome,dict) or outcome.get('point') is not None: continue
                key=labels.get(str(outcome.get('name','')).strip().casefold())
                if key is None: continue
                try: price=float(outcome.get('price'))
                except (ValueError,TypeError): continue
                if not math.isfinite(price) or price<=1: continue
                if key in prices: duplicate=True
                prices[key]=price
            if duplicate or set(prices)!={'home_draw','draw_away','home_away'}: continue
            total=sum(1/x for x in prices.values())
            if not 1.96<=total<=2.40: continue
            fair={k:2/(v*total) for k,v in prices.items()}
            if any(p>1 for p in fair.values()): continue
            stamp=str(market.get('last_update') or book.get('last_update') or '')
            offers.append((stamp,name,prices,fair))
    if not offers: return {}
    ref=max(offers,key=lambda x:x[0]);out={}
    for key in MARKETS:
        from quote_policy import usable_bookmaker
        usable=[x for x in offers if usable_bookmaker(x[1])]
        best=max(usable,key=lambda x:x[2][key]) if usable else (None,None,{key:None})
        out.update({f'market_p_{key}':ref[3][key],f'market_{key}_odds':best[2][key],
                    f'best_{key}_bookmaker':best[1],
                    f'market_best_{key}_last_update_utc':best[0] or None,
                    f'market_reference_{key}_last_update_utc':ref[0] or None,
                    f'market_{key}_bookmakers':len({x[1] for x in usable}),
                    f'market_reference_{key}_method':'proportional_overlap_sum_two'})
    for key,price in ref[2].items():
        out[f'market_reference_dc_{key}_odds']=price
    return out
