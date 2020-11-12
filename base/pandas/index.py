# 索引和选择数据
#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
                  index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], columns=['A', 'B', 'C', 'D'])
print(df)
# loc 基于标签的索引
print(df.loc[:, 'A'])
print(df.loc[:, ['A', 'B']])
print(df.loc[['a', 'b'], ['A', 'B']])
print(df.loc['a':'b'])
print(df.loc['a'] > 0)

# iloc基于整数的索引
print(df.iloc[:4])
print(df.iloc[1:5, 2:4])

# ix 混合标签和整数索引
print(df.ix[:4])
print(df.ix[:, 'A'])

# 直接引用
print(df['A'])
print(df.A)
print(df[2:5])
