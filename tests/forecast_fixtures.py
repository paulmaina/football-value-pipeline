"""Small forecast fixtures shared by several tests.

Moved here unchanged from the retired experiments' test modules (removed 25 Nov 2026 with archive/), which
other tests imported them from. tuning() is dc_decay_validation.tune_half_life on the toy history, without the
archived recency diagnostics that nothing live reads.
"""
from datetime import datetime, timedelta, timezone

import numpy as np
import pandas as pd

from dc_decay_validation import tune_half_life
from football_value_pipeline_v2_standalone import reweight_matrix_to_1x2
from historical_benchmark import adjusted_matrix, goals
from test_conservative_bet_filter import fixture

NOW = datetime(2026, 10, 15, 9, tzinfo=timezone.utc)


def frame():
    row=fixture(kickoff=NOW+timedelta(days=1));row.update(home_team='Manchester City FC',away_team='Everton FC',
        model_home_team='Manchester City FC',model_away_team='Everton FC',market_weight=.5,market_source_1x2='The Odds API / Pinnacle',
        odds_h2h_last_update_utc=(NOW-timedelta(minutes=5)).isoformat())
    for k,p in zip(('home','draw','away'),(.69,.185,.125)):row['p_'+k]=p
    return pd.DataFrame([row])


def simplex(row,prefix):
    from performance_tracking import number
    p=[number(row.get(prefix+k),min_value=0,max_value=1) for k in ('home','draw','away')]
    return p if all(v is not None for v in p) and abs(sum(p)-1)<1e-6 else None


def sample():
    row=frame().iloc[0].to_dict();row.update(lambda_home=1.7,lambda_away=.9,odds_event_id='abc')
    m=reweight_matrix_to_1x2(adjusted_matrix(1.7,.9,-.04,10),simplex(row,'p_'))
    for k,v in goals(m).items():row['p_'+k]=v
    ref={'bookmaker':'pinnacle','updated_at_utc':NOW.isoformat(),'over':1.95,'under':1.95,'event_id':'abc','kickoff_utc':row['kickoff_utc'],'home_team':row['home_team'],'away_team':row['away_team']}
    inputs={'lambda_home':1.7,'lambda_away':.9,'rho':-.04,'max_goals':10,'reference':ref}
    return row,m,inputs


def history():
    return pd.DataFrame({'Date':pd.date_range('2023-01-01',periods=130,freq='7D'),
        'HomeTeam':['A']*130,'AwayTeam':['B']*130,'FTHG':[2]*130,'FTAG':[1]*130})


class ToyModel:
    fits=[]; matrices=0
    def __init__(self,half_life_days,l2,max_goals):self.half=half_life_days
    def fit(self,data,as_of=None):
        if as_of is not None: assert data.Date.max()<as_of
        self.fits.append((self.half,len(data),as_of));return self
    def score_matrix(self,home,away):
        type(self).matrices+=1
        p=.4 if self.half==120 else .8
        matrix=np.zeros((3,3));matrix[0,0]=1-p;matrix[2,1]=p
        return matrix,{'home_name_match_score':100,'away_name_match_score':100}
    def one_x_two(self,matrix):
        return {'home':.8,'draw':.1,'away':.1} if self.half==120 else {'home':.4,'draw':.3,'away':.3}


def tuning():
    return tune_half_life(history(),ToyModel,candidates=[120,240],l2=.08,max_goals=10,validation_days=365,
                          step_days=56,min_train=30,min_validation_matches=5)
