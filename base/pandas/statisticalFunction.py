# 统计功能
#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

# pct_change(periods=1, fill_method=‘pad’, limit=None, freq=None, **kwargs) 表示当前元素与先前periods个元素的相差百分比
s = pd.Series([1, 2, 3, 4, 5, 4])
print(s.pct_change())

df = pd.DataFrame(np.random.randn(5, 2))
print(df.pct_change())

# cov协方差
s1 = pd.Series(np.random.randn(10))
s2 = pd.Series(np.random.randn(10))
print(s1.cov(s2))

frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
print(frame)
print(frame['a'].cov(frame['b']))
print(frame.cov())

# corr 相关性显示任意两个值数组（序列）之间的线性关系。
print(frame['a'].corr(frame['b']))
print(frame.corr())

# 排名
s = pd.Series(np.random.randn(5), index=list('abcde'))
print(s)
# s['d'] = s['b']  # so there's a tie
print(s.rank())
