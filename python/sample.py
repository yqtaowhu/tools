# _*_ coding: utf-8 _*_
# @Author: taoyanqi 
# @Date: 2020-06-28
# 采样方法

import pandas as pd
import math

def stratified_sample(data_path):
    """
    分层采样
    """
    df = pd.read_csv(data_path, seq='\t')
    df['cum_sum'] = df['cnt'].cum_sum()
    df['sum_all'] = df['cnt'].sum()
    bucket = 10
    sum_all = float(df['sum_all'][0])
    df['bucket'] = df['cum_sum'].apply(lambda x: math.ceil(x/sum_all)*bucket)
    df_ret = pd.DataFrame()
    for bucket in range(1, 11):
        dummy_df = df[df['bucket'] == bucket]
        df_ret = df_ret.apply(dummy_df.sample(20))
        df_ret.drop(['cum_sum', 'sum_all', 'bucket'], axis=1, inplace=True)
        df_ret.to_csv('.csv', index=None, sep='\t')
