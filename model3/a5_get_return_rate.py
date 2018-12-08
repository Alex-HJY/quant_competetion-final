# coding=utf-8
from datetime import datetime
from jqdata import macro
from jqdata import *
import matplotlib.pyplot as plt
from datetime import timedelta
import pandas as pd
from dateutil import parser
from WindPy import *


ZHOUQI = ['复苏', '过热', '滞涨', '衰退']



def get_wind_data(start, end):
    df=w.wss("801011.SI,801012.SI,801013.SI,801014.SI,801015.SI,801016.SI,801017.SI,801018.SI,801021.SI,801022.SI,801023.SI,801024.SI,801032.SI,801033.SI,801034.SI,801035.SI,801036.SI,801037.SI,801041.SI,801051.SI,801053.SI,801054.SI,801055.SI,801072.SI,801073.SI,801074.SI,801075.SI,801076.SI,801081.SI,801082.SI,801083.SI,801084.SI,801085.SI,801092.SI,801093.SI,801094.SI,801101.SI,801102.SI,801111.SI,801112.SI,801123.SI,801124.SI,801131.SI,801132.SI,801141.SI,801142.SI,801143.SI,801151.SI,801152.SI,801153.SI,801154.SI,801155.SI,801156.SI,801161.SI,801162.SI,801163.SI,801164.SI,801171.SI,801172.SI,801173.SI,801174.SI,801175.SI,801176.SI,801177.SI,801178.SI,801181.SI,801182.SI,801191.SI,801192.SI,801193.SI,801194.SI,801202.SI,801203.SI,801204.SI,801205.SI,801211.SI,801212.SI,801213.SI,801214.SI,801215.SI,801222.SI,801223.SI,801231.SI,801711.SI,801712.SI,801713.SI,801721.SI,801722.SI,801723.SI,801724.SI,801725.SI,801731.SI,801732.SI,801733.SI,801734.SI,801741.SI,801742.SI,801743.SI,801744.SI,801751.SI,801752.SI,801761.SI,801881.SI",
             "pct_chg_per,sec_name","startDate="+start+";endDate="+end,usedf=True)[1]
    df=df.set_index('SEC_NAME')
    df.columns=[start+'-'+end]
    df.index.name='code'
    return df


def get_paiming(df=pd.DataFrame([]),trend=''):
    number_of_time = df.__len__()
    dff=pd.DataFrame()
    for i in range(number_of_time):
        start_time = df.iloc[i]['start']
        end_time = df.iloc[i]['end']
        dff=dff.join(get_wind_data(start_time,end_time),how='right')

    df.dropna(inplace=True)
    # dff = dff[dff.index.map(int) > 2000012551000000]
    dff.to_csv('./data/wind/'+trend.decode('utf-8')+'.csv',encoding='utf-8-sig')
    return []


if __name__ == '__main__':
    w.start()

    df = pd.read_csv('./data/zhouqiqujian.csv', index_col='id')
    df = df.sort_values('trend')
    df['start']=df['start'].map(parser.parse)
    df['end']=df['end'].map(parser.parse)
    df['start'] = df['start'].map(lambda  x:x.strftime('%Y%m%d'))
    df['end'] = df['end'].map(lambda  x:x.strftime('%Y%m%d'))
    for trend in ZHOUQI:
        get_paiming(df[df['trend'] ==trend],trend)

    w.close()
