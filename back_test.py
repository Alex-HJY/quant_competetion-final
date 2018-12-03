import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta
from dateutil import parser
from datetime import datetime
import trade_funcs


def calc_bench(df=pd.DataFrame(), bench_mark='', start_date='', end_date='', start_money=10000):
    """
    :param df: 股票日线数据
    :param bench_mark: 基准列名
    :param start_date: 起始日期
    :param end_date: 结束日期
    :param start_money: 初始金钱
    :return: 基准收益序列
    """
    return df


def back_test_by_day(df=pd.DataFrame(), bench_mark='', target='', start_date='', end_date='', start_money=10000
                     , trade_func='', save_path=''):
    """
    回测函数
    :param df: 股票日线数据
    :param bench_mark: 基准列名
    :param target: 标的名
    :param start_date: 起始日期
    :param end_date: 结束日期
    :param start_money: 初始金钱
    :param trade_func: 交易函数
    :param save_path: 保存路径
    :return: 回测结果
    """

    # 设定初始参数
    money = start_money
    cash = 0
    portfolio = {}
    df = df
    result = pd.DataFrame()
    start_date = parser.parse(start_date)
    end_date = parser.parse(end_date)
    day = timedelta(days=1)
    today = start_date

    # 按天回测
    while today < end_date:
        money, cash, portfolio = result.append(trade_func(df, today, target, money, cash, portfolio))
        today = today + day

    # 计算基准收益并整合
    if bench_mark != '':
        bench_profit = calc_bench(df, bench_mark, start_date, end_date, start_money)
        result = result.join(bench_profit)

    # 输出文件
    if save_path != '':
        result.to_csv(save_path, encoding='utf-8-sig')
    return result


def show_pic(df=pd.DataFrame(), bench_mark='', strategies=[], start_date='', end_date='', start_money=10000):
    """
    画图函数
    :param df: 回测结果数据
    :param bench_mark: 基准列名
    :param start_date: 起始日期
    :param strategies: 策略列名
    :param end_date: 结束日期
    :param start_money: 初始金钱
    :return: None
    """
    return None
