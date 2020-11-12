# 可视化
#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.DataFrame(np.random.randn(10, 4), index=pd.date_range(
    '1/1/2000', periods=10), columns=list('ABCD'))
df.plot()
df.plot.bar()
plt.show()
