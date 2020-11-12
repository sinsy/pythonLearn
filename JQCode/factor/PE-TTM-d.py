import bisect
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from jqdatasdk import *
import time  # 引入time模块
import datetime
auth('13066951909', 'Abao1992')
# 查询是否连接成功
is_auth = is_auth()
print(is_auth)


def get_factor(statDate):
    print(statDate)
    # 获取多只股票在某一日期的市值, 利润

    if '-' in statDate:
        # 获取多只股票在某一日期的市值, 利润
        q1 = query(
            valuation.code, valuation.market_cap, indicator.statDate
        ).filter(
            # 这里不能使用 in 操作, 要使用in_()函数
            valuation.code.in_(stocks)
        )
        df1 = get_fundamentals(q1, date=statDate)
    else:
        # 季度报告
        q1 = query(
            valuation.code, indicator.adjusted_profit,  income.minority_profit, income.net_profit, income.np_parent_company_owners, indicator.statDate
        ).filter(
            # 这里不能使用 in 操作, 要使用in_()函数
            valuation.code.in_(stocks)
        )
        df1 = get_fundamentals(q1, statDate=statDate)

    return df1


code = '000978.XSHG'  # '000978.XSHG' '000016.XSHG' #'000300.XSHG' #399006.XSHE
date = '2019-12-03'  # pd.datetime.today()
# stocks = get_index_stocks(code, date)
stocks = ['000028.XSHE', '000895.XSHE']
q = query(valuation, indicator).filter(valuation.code.in_(stocks))
df = get_factor(date)
ticks = str(time.time())

# 计算方法6：PE-TTM也称之为滚动市盈率。TTM英文本意是Trailing Twelve Months，也就是过去12个月，
# 非常好理解，比如当前2017年半年报刚发布完，那么过去12个月的净利润就是：
# 2017Q2(2017年2季报累计值) + 2016Q4(2016年4季度累计值) - 2016Q2(2016年2季度累计值)。
# 根据理杏仁的计算之 市值/12个月的扣非净利润，adjusted_profit目前只拿了一个月的，需要完善
sum_p = 0
sum_e = 0
df_list = []
quarterDf = {
    '03': 'q1',
    '06': 'q2',
    '09': 'q3',
    '12': 'q4'
}
endDate = ""
for i in range(0, 1):
    year = df['statDate'][i][0:4]
    month = df['statDate'][i][5:7]
    lastYear = int(year) - 1
    print(month, year)
    print(quarterDf[month])
    quarter = quarterDf[month]
    if (quarterDf[month] == 'q4'):
        print(month, year)
    else:
        # 过去12个月
        if ('q1' in quarter):
            statDate_list = ['{}{}'.format(
                year, 'q1'), '{}{}'.format(lastYear, 'q2'), '{}{}'.format(lastYear, 'q3'), '{}{}'.format(lastYear, 'q4')]
            endDate = '{}{}'.format(lastYear, '-6-30')
        elif ('q2' in quarter):
            statDate_list = ['{}{}'.format(
                year, 'q1'), '{}{}'.format(year, 'q2'), '{}{}'.format(lastYear, 'q3'), '{}{}'.format(lastYear, 'q4')]
            endDate = '{}{}'.format(lastYear, '-9-30')
        elif ('q3' in quarter):
            statDate_list = ['{}{}'.format(
                year, 'q1'), '{}{}'.format(year, 'q2'), '{}{}'.format(year, 'q3'), '{}{}'.format(lastYear, 'q4')]
            endDate = '{}{}'.format(lastYear, '-12-31')
        elif ('q4' in quarter):
            statDate_list = ['{}{}'.format(
                year, 'q1'), '{}{}'.format(year, 'q2'), '{}{}'.format(year, 'q3'), '{}{}'.format(year, 'q4')]
            endDate = '{}{}'.format(year, '-3-31')

        print(statDate_list)
        for statDate in statDate_list:
            df_temp = get_factor(statDate)
            df_list.append(df_temp)
fac_df = pd.concat(df_list)
# print(fac_df)
fac_df_sum = fac_df.groupby(
    'code')['adjusted_profit', 'minority_profit'].sum().reset_index()
# print(df)
print(fac_df_sum)
merge_df = pd.merge(df, fac_df_sum)
merge_df['PE-TTM'] = merge_df['market_cap'] * \
    100000000/(merge_df['adjusted_profit']-merge_df['minority_profit'])
print(merge_df)

fac_df.to_csv('C:/data/' + ticks + '.csv', encoding='utf_8_sig')
