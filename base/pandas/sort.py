# 排序
#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
unsorted_df = pd.DataFrame(np.random.randn(10, 2), index=[
                           1, 4, 6, 2, 3, 5, 9, 8, 0, 7], columns=['col2', 'col1'])
print(unsorted_df)
print(unsorted_df.sort_index())

# 按key值排序
print(unsorted_df.sort_values(by='col1', ascending=False))
