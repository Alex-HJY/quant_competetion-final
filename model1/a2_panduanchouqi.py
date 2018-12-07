#coding:utf-8

import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta

economic_df=pd.DataFrame()
dd=economic_df.index

economic_df['cpi_trend']= 'up'
economic_df['growth_trend']= 'down'
month=4

for  i in range(1, economic_df.__len__() - month):
    if economic_df.iloc[i]['CPI当月同比']>economic_df.iloc[i + 1]['CPI当月同比'] and economic_df.iloc[i + 1]['CPI当月同比']>economic_df.iloc[i + 2]['CPI当月同比'] and \
        economic_df.iloc[i + 2]['CPI当月同比'] > economic_df.iloc[i + 3]['CPI当月同比'] :
        economic_df.ix[i, 'cpi_trend']= 'down'
        continue

    if economic_df.iloc[i]['CPI当月同比']<economic_df.iloc[i + 1]['CPI当月同比'] and economic_df.iloc[i + 1]['CPI当月同比']<economic_df.iloc[i + 2]['CPI当月同比'] and \
        economic_df.iloc[i + 2]['CPI当月同比'] < economic_df.iloc[i + 3]['CPI当月同比'] :
        economic_df.ix[i, 'cpi_trend']= 'up'
        continue

    if economic_df.iloc[i]['CPI当月同比']>max(economic_df.iloc[i + 1]['CPI当月同比'], economic_df.iloc[i + 2]['CPI当月同比'] , economic_df.iloc[i + 3]['CPI当月同比']) \
        and economic_df.iloc[i + month]['CPI当月同比']<min(economic_df.iloc[i + 1]['CPI当月同比'], economic_df.iloc[i + 2]['CPI当月同比'] , economic_df.iloc[i + 3]['CPI当月同比']):
        economic_df.ix[i, 'cpi_trend']= 'down'
        continue

    if economic_df.iloc[i]['CPI当月同比'] < min(economic_df.iloc[i + 1]['CPI当月同比'], economic_df.iloc[i + 2]['CPI当月同比'], economic_df.iloc[i + 3]['CPI当月同比']) \
            and economic_df.iloc[i + month]['CPI当月同比'] > max(economic_df.iloc[i + 1]['CPI当月同比'], economic_df.iloc[i + 2]['CPI当月同比'], economic_df.iloc[i + 3]['CPI当月同比']):
        economic_df.ix[i, 'cpi_trend'] = 'up'
        continue
    economic_df.ix[i, 'cpi_trend']=economic_df.iloc[i - 1]['cpi_trend']

for  i in range(1, economic_df.__len__() - month):
    if economic_df.iloc[i]['宏观经济景气指数一致指数']>economic_df.iloc[i + 1]['宏观经济景气指数一致指数'] and economic_df.iloc[i + 1]['宏观经济景气指数一致指数']>economic_df.iloc[i + 2]['宏观经济景气指数一致指数'] and \
        economic_df.iloc[i + 2]['宏观经济景气指数一致指数'] > economic_df.iloc[i + 3]['宏观经济景气指数一致指数'] :
        economic_df.ix[i, 'growth_trend']= 'down'
        continue

    if economic_df.iloc[i]['宏观经济景气指数一致指数']<economic_df.iloc[i + 1]['宏观经济景气指数一致指数'] and economic_df.iloc[i + 1]['宏观经济景气指数一致指数']<economic_df.iloc[i + 2]['宏观经济景气指数一致指数'] and \
        economic_df.iloc[i + 2]['宏观经济景气指数一致指数'] < economic_df.iloc[i + 3]['宏观经济景气指数一致指数'] :
        economic_df.ix[i, 'growth_trend']= 'up'
        continue

    if economic_df.iloc[i]['宏观经济景气指数一致指数']>max(economic_df.iloc[i + 1]['宏观经济景气指数一致指数'], economic_df.iloc[i + 2]['宏观经济景气指数一致指数'] , economic_df.iloc[i + 3]['宏观经济景气指数一致指数']) \
        and economic_df.iloc[i + month]['宏观经济景气指数一致指数']<min(economic_df.iloc[i + 1]['宏观经济景气指数一致指数'], economic_df.iloc[i + 2]['宏观经济景气指数一致指数'] , economic_df.iloc[i + 3]['宏观经济景气指数一致指数']):
        economic_df.ix[i, 'growth_trend']= 'down'
        continue

    if economic_df.iloc[i]['宏观经济景气指数一致指数'] < min(economic_df.iloc[i + 1]['宏观经济景气指数一致指数'], economic_df.iloc[i + 2]['宏观经济景气指数一致指数'], economic_df.iloc[i + 3]['宏观经济景气指数一致指数']) \
            and economic_df.iloc[i + month]['宏观经济景气指数一致指数'] > max(economic_df.iloc[i + 1]['宏观经济景气指数一致指数'], economic_df.iloc[i + 2]['宏观经济景气指数一致指数'], economic_df.iloc[i + 3]['宏观经济景气指数一致指数']):
        economic_df.ix[i, 'growth_trend'] = 'up'
        continue
    economic_df.ix[i, 'growth_trend']=economic_df.iloc[i - 1]['growth_trend']

economic_df.ix['trend']= ''

for  i in range(1, economic_df.__len__() - month):
    if economic_df.ix[i, 'growth_trend']== 'up':
        if economic_df.ix[i, 'cpi_trend']== 'up':
            economic_df.ix[i, 'trend']= '过热'
        else:
            economic_df.ix[i, 'trend'] = '复苏'
    else:
        if economic_df.ix[i, 'cpi_trend']== 'up':
            economic_df.ix[i, 'trend']= '滞涨'
        else:
            economic_df.ix[i, 'trend'] = '衰退'

economic_df= economic_df[:-1]
economic_df.index=dd
economic_df= economic_df['2005':]
economic_df.to_csv('./data/zhouqi_joinquant.csv', encoding='utf-8_sig')

print economic_df
