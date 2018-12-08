import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta
from dateutil import parser
from datetime import datetime
import back_test

TIME_TO_BUT = {'衰退': ['证券', '保险'],
               '滞涨': ['通信运营', '船舶制造'],
               '复苏': ['房地产开发', '汽车整车'],
               '过热': ['工业金属', '环保工程及服务'],
               'HS300': ['hs300']}

def trade_model1(df_to_today, today, money, cash, portfolio):
    df_to_today.loc[today]




    return money, cash, portfolio


close_df=pd.read_csv('./data/index_close.csv',encoding='utf-8-sig')
backtest1=back_test.back_test_system(close_df,'',save_dir='./model1/')