#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
                  index=pd.date_range('1/1/2000', periods=10),
                  columns=['A', 'B', 'C', 'D'])
print(df)
r = df.rolling(window=3, min_periods=1)
print(r)
print(r.aggregate(np.sum))


# 单列
print(r['A'].aggregate(np.sum))

# 应用多个功能
print(r[['A', 'B']].aggregate([np.sum, np.mean]))
print(r[['A', 'B']].aggregate({'A': np.sum, 'B': np.mean}))
