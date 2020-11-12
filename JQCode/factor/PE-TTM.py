import bisect
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from jqdatasdk import *
import time  # 引入time模块
import datetime
auth('13066951909', 'Abao6883544')
# 查询是否连接成功
is_auth = is_auth()
print(is_auth)


def get_factor(statDate):
    print(statDate)
    # 获取多只股票在某一日期的市值, 利润

    if '-' in statDate:
        # 获取多只股票在某一日期的市值, 利润
        q1 = query(
            valuation.code, valuation.market_cap, valuation.pe_ratio, indicator.statDate
        ).filter(
            # 这里不能使用 in 操作, 要使用in_()函数
            valuation.code.in_(stocks)
        )
        df1 = get_fundamentals(q1, date=statDate)
    else:
        # 季度报告
        q1 = query(
            valuation.code, indicator.adjusted_profit,  indicator.statDate
        ).filter(
            # 这里不能使用 in 操作, 要使用in_()函数
            valuation.code.in_(stocks)
        )
        df1 = get_fundamentals(q1, statDate=statDate)

    return df1


# '000978.XSHG' '000016.XSHG' #'000300.XSHG' #399006.XSHE
# code = ['000300.XSHG', '000978.XSHG',
#         '000015.XSHG', '000919.XSHG', '000922.XSHG']
code = ['000978.XSHG']
date = '2019-12-03'  # pd.datetime.today()
data = {}
for i in code:
    stocks = get_index_stocks(i, date)
    df = get_factor(date)
    df['e'] = df['market_cap'] / df['pe_ratio']
    peTTM = df['market_cap'].sum() / df['e'].sum()
    data[i] = peTTM

print(data)
# ticks = str(time.time())
# df.to_csv('C:/data/' + ticks + '.csv', encoding='utf_8_sig')
