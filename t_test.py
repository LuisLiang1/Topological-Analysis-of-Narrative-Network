#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 16:20:30 2022

@author: luisliang
"""

from scipy import stats
import numpy as np
import pandas as pd

# Count the number of nodes
def topic_count(target_list):
    tc=[]
    for i in range(len(target_list)):
        tc.append(pd.DataFrame(pd.value_counts(target_list[i])).reset_index())
    return tc

# Merge all the list together
def merge_list(df_list):
    key='index'
    result=df_list[0]
    for i in range(1,len(df_list)):
        df_list[i]=df_list[i].rename(columns={0:i})
        result=pd.merge(result,df_list[i],on=key,how="outer")
    return result    

# Build T-test Process
def t_test(sample1,sample2):
    sample1 = np.asarray(sample1)
    sample2 = np.asarray(sample2)
    r = stats.ttest_ind(sample1, sample2)
    p_value=r.__getattribute__("pvalue")
    sta=r.__getattribute__("statistic")
    return p_value,sta

# Calculate the p-value
def calculate_p(list):
    result=[]
    for i in range(len(list)):
        section=[]
        section.append(list[i][0])
        sample1=list[i][36:len(list)-1]
        sample2=list[i][1:35]
        p,sta=t_test(sample1,sample2)
        section.append(p)
        section.append(sta)
        result.append(section)
    return result

# Split data into small sections
def split_data(num_of_each,column_df):
    chunks_number=int(len(column_df)/num_of_each)
    target_list=[[] for i in range(chunks_number)]
    column_name=column_df.columns[0]
    for i in range(num_of_each*chunks_number):
        for j in range(chunks_number):
            if i%chunks_number==j:
                target_list[j].append(column_df[column_name][i])
    return target_list