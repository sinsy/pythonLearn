#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import pandas as pd

# 合并pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,left_index = False, right_index = False, sort = True)
left = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id': ['sub1', 'sub2', 'sub4', 'sub6', 'sub5']})
right = pd.DataFrame(
    {'id': [1, 2, 3, 4, 5],
     'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
     'subject_id': ['sub2', 'sub4', 'sub3', 'sub6', 'sub5']})
print(left)
print(right)
# 单键
print(pd.merge(left, right, on='id'))
# 多键
print(pd.merge(left, right, on=['id', 'subject_id']))

# 左加入，以左边的为准，填充右边没有的，去掉右边有的
print(pd.merge(left, right, on='subject_id', how='left'))

# 外连接,并集
print(pd.merge(left, right, on='subject_id', how='outer'))

# 内连接，交集
print(pd.merge(left, right, on='subject_id', how='inner'))
