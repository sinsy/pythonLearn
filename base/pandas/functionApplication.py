#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import pandas as pd
import numpy as np


def adder(ele1, ele2):
    return ele1 + ele2


df = pd.DataFrame(np.random.randn(5, 3), columns=['col1', 'col2', 'col3'])
print(df)

# pipe 表格函数应用
print(df.pipe(adder, 2))

# apply 表格行列行数应用
print(df.apply(np.mean))

# applymap 表格元素应用
print(df.applymap(lambda x: x * 100))
print(df[['col1', 'col2']].applymap(lambda x: x * 100))
print(df[0:1].applymap(lambda x: x * 100))
