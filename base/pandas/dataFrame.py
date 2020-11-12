#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import pandas as pd
s = pd.DataFrame()
print(s)

data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data)
print(df)

data1 = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df1 = pd.DataFrame(data1, columns=['Name', 'Age'], dtype=float)
print(df1)

# 使用数组创建索引的DataFrame
data2 = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28, 34, 29, 42]}
df2 = pd.DataFrame(data2, index=['rank1', 'rank2', 'rank3', 'rank4'])
print(df2)

# 使用数据字典创建DataFrame
data3 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df3 = pd.DataFrame(data3)
print(df3)

# 从系列字典创建一个DataFrame
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df4 = pd.DataFrame(d)
print(df4)

# 列选择
print(df4['one'])

# 列添加
df4['three'] = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(df4)

# 列删除 del or pop
del df4['one']
# df4.pop('one')
print(df4)

# 行选择
print(df4.loc['a'])

# 切片行
print('切片行')
print(df4[2:4])

# 删除行
df4.drop('a')
print(df4)

# 行加法
df_a1 = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
df_a2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a', 'b'])
df_a = df_a1.append(df_a2)
print(df_a)
