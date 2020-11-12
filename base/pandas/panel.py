#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

# panel属性被移走了，不用看了

data = np.random.rand(2, 4, 5)
print(data)
p = pd.Panel()
print(p)
