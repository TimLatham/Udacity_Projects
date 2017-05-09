# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:13:43 2017

@author: tim.latham
"""

# Import libraries
import pandas as pd

loan_data = pd.read_csv("loan.csv", low_memory=False)
print(float(len(loan_data)))
print (loan_data.head())

loan_data = loan_data.drop(loan_data[(loan_data.loan_status != 'Fully Paid') & (loan_data.loan_status != 'Charged Off')].index)

print(float(len(loan_data)))

dropFields = ['acc_now_delinq','addr_state','all_util','annual_inc_joint','application_type',
              'collection_recovery_fee','desc','dti_joint','emp_title',
              'funded_amnt_inv','grade','id','il_util','initial_list_status',
              'inq_fi','inq_last_12m','int_rate','issue_d','last_credit_pull_d',
              'last_pymnt_amnt','last_pymnt_d','loan_amnt','max_bal_bc','member_id',
              'mths_since_rcnt_il','next_pymnt_d','open_acc_6m','open_il_12m',
              'open_il_24m','open_il_6m','open_rv_12m','open_rv_24m','out_prncp',
              'out_prncp_inv','policy_code','pymnt_plan','recoveries','revol_bal',
              'sub_grade','title','tot_coll_amt','tot_cur_bal','total_acc',
              'total_bal_il','total_cu_tl','total_pymnt','total_pymnt_inv',
              'total_rec_int','total_rec_late_fee','total_rec_prncp',
              'total_rev_hi_lim','url','verification_status_joint','zip_code']

loan_data = loan_data.drop(dropFields, axis=1)
loan_data = loan_data.drop(loan_data[(loan_data.home_ownership != 'RENT') & (loan_data.home_ownership != 'OWN') & (loan_data.home_ownership != 'MORTGAGE')].index)

#print(loan_data.collections_12_mths_ex_med.unique())
loan_data = loan_data[pd.notnull(loan_data['collections_12_mths_ex_med'])]
loan_data = loan_data[pd.notnull(loan_data['revol_util'])]
#print(loan_data.loan_status.unique())
loan_data.ix[loan_data.loan_status == 'Charged Off', 'loan_status'] = 1
loan_data.ix[loan_data.loan_status == 'Fully Paid', 'loan_status'] = 0
#print(loan_data.loan_status.unique())





print (loan_data.head())
print(float(len(loan_data)))

print(loan_data.term.unique())
loan_data.ix[loan_data.term == '60 Month', 'term'] = 1
loan_data.ix[loan_data.term == '36 Month', 'term'] = 0
print(loan_data.term.unique())