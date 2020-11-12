# 丢失数据
#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
                                                'h'], columns=['one', 'two', 'three'])
print(df)
df = df.reindex(['a', 'q'])
print(df)

# 检验是否丢失
print(df['one'].isnull())
print(df['one'].notnull())

# 缺少数据的计算 汇总数据时，NA将被视为零
print(df['one'].sum())

# 用标量值替换NaN
print(df.fillna(0))
