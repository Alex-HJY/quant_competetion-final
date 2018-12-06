from copy import deepcopy

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta
from dateutil import parser
from datetime import datetime


class back_test_system:
    def __init__(self, df=pd.DataFrame(), bench_mark='', start_money=1000000, save_dir=''):
        self.close_df = deepcopy(df)
        self.bench_mark = bench_mark
        self.start_money = start_money
        self.save_dir = save_dir

    def calc_bench(self, start_date='', end_date=''):
        """

        :param start_date: 起始日期 datetime
        :param end_date: 结束日期 datetime
        :return:
        """
        close_df = self.close_df
        df = pd.DataFrame()
        one_day = timedelta(days=1)
        date_now = start_date
        while date_now < end_date:
            if date_now not in close_df.index:
                date_now = date_now + one_day
            else:
                break

        share = self.start_money / close_df.loc[date_now, self.bench_mark + '_close']

        while date_now < end_date:
            if date_now in close_df.index:
                df.append(
                    pd.DataFrame(
                        data=[
                            [share * close_df.loc[date_now, self.bench_mark + '_close'], {self.bench_mark: share}, 0]],
                        index=[date_now],
                        columns=[self.bench_mark + '_money', self.bench_mark + '_portfolio',
                                 self.bench_mark + '_cash']))
            else:
                date_now=date_now+one_day

        return close_df

    def back_test_by_day(self, strategy_name='', trade_func=function(), save_path='', start_date='', end_date=''):
        """

        :param strategy_name:
        :param trade_func:
        :param save_path:
        :param start_date:
        :param end_date:
        :return:
        """

        # 设定初始参数
        money = self.start_money
        cash = 0
        portfolio = {}
        df = pd.DataFrame()
        result = pd.DataFrame()
        day = timedelta(days=1)
        today = start_date
        bench_mark = self.bench_mark
        target = self.target

        # 按天回测
        while today < end_date:
            df = df.append(self.close_df.loc[today])
            money, cash, portfolio = result.append(trade_func(df, today, loc, target, money, cash, portfolio))
            today = today + day

        # 计算基准收益并整合
        if bench_mark != '':
            bench_profit = self.calc_bench()
            result = result.join(bench_profit)

        # 输出文件
        if save_path != '':
            result.to_csv(save_path, encoding='utf-8-sig')
        return result

    def show(self, strategies_name=[], start_date='', end_date='',
             start_money=1000000):
        """

        :param strategies_name:
        :param start_date:
        :param end_date:
        :param start_money:
        :return:
        """
        df = self.close_df
        return None

    def get_indexes(self, strategies_name=[], start_date='', end_date=''):
        indexes = self.close_df
        return indexes
