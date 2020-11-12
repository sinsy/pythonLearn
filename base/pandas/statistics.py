#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

# Descriptive Statistics 统计方法

d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack',
                        'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])
     }
df = pd.DataFrame(d)
print(df)

# sum
print(df.sum())

# axis=1 sum(1)则计算每一行的向量之和
print(df.sum(1))

# mean() 返回平均值
print(df.mean())

# std() 返回数值列的Bressel标准偏差
print(df.std())

# 汇总所有数据
print(df.describe())

# 'zero': 0 zero列的全是0
d1 = {'up_pct': [-1, 2, 3, 4], 'zero': 0}
df1 = pd.DataFrame(d1)
print(df1.max(1))
