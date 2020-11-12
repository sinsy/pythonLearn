#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

# Reindexing重新索引
N = 20
df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01', periods=N, freq='D'),
    'x': np.linspace(0, stop=N-1, num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low', 'Medium', 'High'], N).tolist(),
    'D': np.random.normal(100, 10, size=(N)).tolist()
})
print(df)

df_reindex = df.reindex(index=[0, 2, 5], columns=['A', 'C', 'B'])
print(df_reindex)
