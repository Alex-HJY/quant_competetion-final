import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta
from dateutil import parser
from datetime import datetime
import back_test
import numpy as np
from dateutil.relativedelta import relativedelta

dir_name = 'model3'

TIME_TO_BUT = {'衰退': ['证券', '保险'],
               '滞涨': ['通信运营', '船舶制造'],
               '复苏': ['房地产开发', '汽车整车'],
               '过热': ['工业金属', '环保工程及服务'],
               'HS300': ['hs300']}



#Model1 轮动策略交易函数
def trade_model1(df_to_today, today, money, cash, portfolio):
    df_to_today.loc[today]
    df = pd.read_csv('./trends.csv', encoding='utf-8-sig', index_col='DateTime')
    df.index = df.index.map(lambda x: x[:-3])
    trend = df.loc[today.strftime('%Y')+'-'+today.strftime('%m')]['trend']

    df = pd.read_csv('./'  + trend + '_sort.csv', encoding='utf-8-sig', engine='python',
                     index_col='code')
    targets = [df.index[0], df.index[1]]
    df=pd.read_csv('../data/code_to_name.csv',engine='python',encoding='utf-8-sig',index_col='SEC_NAME')

    for obj,share in portfolio.items():
        cash+=df_to_today[df.loc[obj]['code']][-1]*share

    portfolio={}

    cash_share=(cash / targets.__len__())
    for target in targets:

        if pd.notna(df_to_today[df.loc[target]['code']][-1]):
            portfolio[target]=cash_share/df_to_today[df.loc[target]['code']][-1]
            cash-=cash_share

    money=cash

    for key,value in portfolio.items():
        money+=df_to_today[df.loc[key]['code']][-1]*value

    # print(today, money, cash, portfolio)
    return money, cash, portfolio

def trade_model2_3month(df_to_today, today, money, cash, portfolio):
    df_to_today.loc[today]
    df = pd.read_csv('./trends.csv', encoding='utf-8-sig', index_col='DateTime')
    df.index = df.index.map(lambda x: x[:-3])
    trend = df.loc[today.strftime('%Y')+'-'+(today-relativedelta(months=3)).strftime('%m')]['trend']

    df = pd.read_csv('./'  + trend + '_sort.csv', encoding='utf-8-sig', engine='python',
                     index_col='code')
    targets = [df.index[0], df.index[1]]
    df=pd.read_csv('../data/code_to_name.csv',engine='python',encoding='utf-8-sig',index_col='SEC_NAME')

    for obj,share in portfolio.items():
        cash+=df_to_today[df.loc[obj]['code']][-1]*share

    portfolio={}

    cash_share=(cash / targets.__len__())
    for target in targets:

        if pd.notna(df_to_today[df.loc[target]['code']][-1]):
            portfolio[target]=cash_share/df_to_today[df.loc[target]['code']][-1]
            cash-=cash_share

    money=cash

    for key,value in portfolio.items():
        money+=df_to_today[df.loc[key]['code']][-1]*value

    # print(today, money, cash, portfolio)
    return money, cash, portfolio


close_df = pd.read_csv('../data/index_close.csv', encoding='utf-8-sig',index_col='DateTime')
close_df.index=pd.DatetimeIndex(close_df.index)
backtest1 = back_test.back_test_system(close_df, 'hs300', save_dir='./back_test/')
df=backtest1.back_test_by_day('lundong',trade_model1,'20100101','20171231')
df=backtest1.back_test_by_day('lundong_3month',trade_model2_3month,'20100101','20171231')
backtest1.show(df=df,strategies_name=['lundong','lundong_3month'])