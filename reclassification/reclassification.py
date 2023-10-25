#author: Theodore Morley
#Date: Oct 25th 2023
import pandas as pd

def calculate_nri(outcome, prob_new, prob_old, cutoff):
    '''
    Input: Series with new probabilities, series with old probabilities, series with outcome, cutoff for NRI calculation.
    Output: NRI
    Note: If cutoff is set to zero, this constitutes "continuous NRI".
    '''
    t_df = pd.DataFrame()
    t_df['new_prob'] = prob_new
    t_df['old_prob'] = prob_old
    t_df['outcome'] = outcome
    t_df['updown'] = 0
    t_df.loc[((t_df.new_prob-cutoff)>t_df.old_prob), 'updown']=1
    t_df.loc[((t_df.new_prob+cutoff)<t_df.old_prob), 'updown']=-1
    casenum=t_df.loc[t_df.outcome==1].shape[0]
    controlnum=t_df.loc[t_df.outcome==0].shape[0]
    try:
        nri = (t_df.loc[(t_df.outcome==1)&(t_df.updown==1)].shape[0]/casenum-t_df.loc[(t_df.outcome==1)&(t_df.updown==-1)].shape[0]/casenum)+((t_df.loc[(t_df.outcome==0)&(t_df.updown==-1)].shape[0]/controlnum-t_df.loc[(t_df.outcome==0)&(t_df.updown==1)].shape[0]/controlnum))
    except:
        raise Exception("NRI undefined in this circumstance")
    return nri

def calculate_idi_colname(probs, colname_cc, colname_prob_new, colname_prob_old):
    '''
    Input: Dataframe containing outcome (named colname_cc), new probabilities (colname_prob_new), and old probabilities (named colname_prob_old), and those column names.
    Output: IDI
    ''' 
    meanCaseNew = probs.loc[probs[colname_cc]==1, colname_prob_new].mean()
    meanControlNew = probs.loc[probs[colname_cc]==0, colname_prob_new].mean()
    meanCaseOld = probs.loc[probs[colname_cc]==1, colname_prob_old].mean()
    meanControlOld = probs.loc[probs[colname_cc]==0, colname_prob_old].mean()
    idi = (meanCaseNew-meanControlNew)-(meanCaseOld-meanControlOld)
    return idi

def calculate_idi(case_status, new_probabilities, old_probabilities):
    '''
    Input: Series containing case_status, series containing new probabilities, series containing old probabilities.
    Output: IDI
    '''
    #set up working dataframe
    t_df = pd.DataFrame()
    t_df['new_prob']=new_probabilities
    t_df['old_prob']=old_probabilities
    t_df['outcome']=case_status
    #calculate means
    meanCaseNew = t_df.loc[t_df['outcome']==1, 'new_prob'].mean()
    meanControlNew = t_df.loc[t_df['outcome']==0, 'new_prob'].mean()
    meanCaseOld = t_df.loc[t_df['outcome']==1, 'old_prob'].mean()
    meanControlOld = t_df.loc[t_df['outcome']==0, 'old_prob'].mean()
    idi = (meanCaseNew-meanControlNew)-(meanCaseOld-meanControlOld)
    return idi

