from copy import deepcopy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta
from dateutil import parser
from datetime import datetime


class back_test_system:
    def __init__(self, close_df=pd.DataFrame(), bench_mark='', start_money=1000000, save_dir=''):
        """

        :param close_df: 收盘价数据
        :param bench_mark: 基准收益标的名称
        :param start_money: 起始现金
        :param save_dir: 储存目录
        """
        self.close_df = deepcopy(close_df)
        self.bench_mark = bench_mark
        self.start_money = start_money
        self.save_dir = save_dir
        self.result = pd.DataFrame()

    def calc_bench(self, start_date='', end_date=''):
        """
        计算基本收益率
        :param start_date: 起始日期 datetime
        :param end_date: 结束日期 datetime
        :return: DataFrame, columns = [cash,money,portfolio]
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
                df = df.append(
                    pd.DataFrame(
                        data=[
                            [share * close_df.loc[date_now, self.bench_mark + '_close'], {self.bench_mark: share}, 0]],
                        index=[date_now],
                        columns=[self.bench_mark + '_money', self.bench_mark + '_portfolio',
                                 self.bench_mark + '_cash']))
            else:
                date_now = date_now + one_day

        return df

    def back_test_by_day(self, strategy_name='', trade_func=function(), start_date='', end_date=''):
        """

        :param strategy_name: 策略名称
        :param trade_func: 交易函数，函数参数为close_data, today,  money, cash, portfolio
        :param start_date: 起始日期
        :param end_date: 结束日期
        :return: df 包含策略的 CASH,MONEY,PORTFOLIO
        """

        # 设定初始参数
        close_data = self.close_df
        money = self.start_money
        cash = 0
        portfolio = {}
        df_to_today = pd.DataFrame()
        result = pd.DataFrame()
        one_day = timedelta(days=1)
        start_date = parser.parse(start_date)
        end_date = parser.parse(end_date)
        today = start_date
        bench_mark = self.bench_mark

        # 按天回测df
        while today < end_date:
            if today in close_data.index:
                df_to_today = df_to_today.append(close_data.loc[today])
                money, cash, portfolio = result.append(trade_func(df_to_today, today, money, cash, portfolio))
            today = today + one_day

        # 计算基准收益并整合
        if bench_mark != '':
            bench_profit = self.calc_bench(start_date, end_date)
            result = result.join(bench_profit)

        # 输出文件
        result.to_csv(self.save_dir + strategy_name + '.csv', encoding='utf-8-sig')
        self.result = result
        return result

    def show(self, strategies_name=[]):
        """
        :param strategies_name:
        :return:
        """
        df = self.result
        for strategy in strategies_name:
            df = pd.read_csv(self.save_dir + strategy + '.csv', encoding='utf-8-sig')
            df.index = pd.DatetimeIndex(df.index)
            plt.plot(df.index, df[strategy + '_money'], label=strategy)
        plt.plot(df.index, df[self.bench_mark + '_money'], label=self.bench_mark)
        plt.legend()
        plt.show()
        return None

    def get_indexes(self, strategies_name=[]):
        indexes = self.close_df
        return indexes
