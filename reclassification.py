import pandas as pd

def calculate_nri(prob_new, prob_old, outcome, cutoff):
    t_df = pd.DataFrame()
    t_df['new_prob'] = prob_new
    t_df['old_prob'] = prob_old
    t_df['outcome'] = outcome
    t_df['updown'] = 0
    t_df.loc[((t_df.new_prob-cutoff)>t_df.old_prob), 'updown']=1
    t_df.loc[((t_df.new_prob+cutoff)<t_df.old_prob), 'updown']=-1
    casenum=t_df.loc[t_df.outcome==1].shape[0]
    controlnum=t_df.loc[t_df.outcome==0].shape[0]
    nri = (t_df.loc[(t_df.outcome==1)&(t_df.updown==1)].shape[0]/casenum-t_df.loc[(t_df.outcome==1)&(t_df.updown==-1)].shape[0]/casenum)+((t_df.loc[(t_df.outcome==0)&(t_df.updown==-1)].shape[0]/controlnum-t_df.loc[(t_df.outcome==0)&(t_df.updown==1)].shape[0]/controlnum))
    return nri

def calculate_idi(probs, colname_cc, colname_prob_new, colname_prob_old):
    meanCaseNew = probs.loc[probs[colname_cc]==1, colname_prob_new].mean()
    meanControlNew = probs.loc[probs[colname_cc]==0, colname_prob_new].mean()
    meanCaseOld = probs.loc[probs[colname_cc]==1, colname_prob_old].mean()
    meanControlOld = probs.loc[probs[colname_cc]==0, colname_prob_old].mean()
    idi = (meanCaseNew-meanControlNew)-(meanCaseOld-meanControlOld)
    return idi