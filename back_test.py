from copy import deepcopy

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta
from dateutil import parser
from datetime import datetime
import trade_funcs


class back_test_system:
    def __init__(self, df=pd.DataFrame(), bench_mark='', start_money=1000000, save_dir=''):
        self.df = deepcopy(df)
        self.bench_mark = bench_mark
        self.start_money = start_money
        self.save_dir = save_dir

    def calc_bench(self, save_path='', start_date='', end_date=''):
        """

        :param end_date:
        :param save_path:
        :param start_date:
        :return:
        """
        df = self.df
        return df

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
        df = self.df
        result = pd.DataFrame()
        day = timedelta(days=1)
        today = start_date
        bench_mark = self.bench_mark
        target = self.target

        # 按天回测
        while today < end_date:
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
        df = self.df
        return None

    def get_indexes(self, strategies_name=[], start_date='', end_date=''):
        indexes = self.df
        return indexes
