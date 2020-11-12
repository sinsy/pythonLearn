# 窗口函数
#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

# rolling
df = pd.DataFrame(np.random.randn(10, 4),
                  index=pd.date_range('1/1/2000', periods=10), columns=['A', 'B', 'C', 'D'])
print(df)
# 3个元素的平均值
print(df.rolling(window=3).mean())
print(df.expanding(min_periods=3).mean())

# ewm 指数分配权重
print(df.ewm(com=0.5).mean())
