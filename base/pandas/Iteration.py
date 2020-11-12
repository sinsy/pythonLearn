# Iteration 迭代

#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

# for循环列key
N = 5
df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01', periods=N, freq='D'),
    'x': np.linspace(0, stop=N-1, num=N),
    'y': np.random.rand(N),
})

for col in df:
    print(col)

# iteritems 遍历（键，值）对
for key, value in df.iteritems():
    print(key, value)

# iterrows 以（index，series）对对行进行迭代
for row_index, row in df.iterrows():
    print(row_index, row)

#itertuples -以namedtuples的形式遍历行
for row in df.itertuples():
    print(row)
# 迭代用于读取，迭代器返回原始对象（视图）的副本，因此更改不会反映在原始对象上。
for index, row in df.iterrows():
    row['a'] = 10
print(df)
