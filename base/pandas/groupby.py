#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import pandas as pd
import numpy as np


ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
                     'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
            'Rank': [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],
            'Year': [2014, 2015, 2014, 2015, 2014, 2015, 2016, 2017, 2016, 2014, 2015, 2017],
            'Points': [876, 789, 863, 673, 741, 812, 756, 788, 694, 701, 804, 690]}
df = pd.DataFrame(ipl_data)

print(df)

# 分割
print(df.groupby('Team').groups)

# 遍历
grouped = df.groupby('Year')
for name, group in grouped:
    print(name)
    print(group)

# 选择一个组
print(grouped.get_group(2015))


# 集合体
print(grouped['Points'].agg(np.mean))

# 多集合体
print(grouped['Points'].agg([np.sum, np.mean]))

# 转变
print(df.groupby('Team').transform(lambda x: (x - x.mean()) / x.std()*10))

# 过滤
print(df.groupby('Team').filter(lambda x: len(x) >= 3))
