'''
https://blog.csdn.net/brucewong0516/article/details/80524442
 DataFrame.plot(x=None, y=None, kind='line', ax=None, subplots=False, 
                sharex=None, sharey=False, layout=None,figsize=None, 
                use_index=True, title=None, grid=None, legend=True, 
                style=None, logx=False, logy=False, loglog=False, 
                xticks=None, yticks=None, xlim=None, ylim=None, rot=None,
                xerr=None,secondary_y=False, sort_columns=False, **kwds)
'''
#%%
import numpy as np
import pandas as pd 

df = pd.DataFrame(np.random.randn(4,4),index = list('ABCD'),columns=list('OPKL'))
print(df)


# %%
df.plot()

# %%
# 散点图，需要传入两个Y的columns参数
df.plot('O', 'L', kind='scatter')

# %%
# 传入x,y参数
df.plot(x='O', y='L', kind="line")

# %%
# 同时设置多个子图，设置subplot=TRUE
df.plot(subplots=True, figsize=(6,6))

# %%
