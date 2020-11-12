#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import pandas as pd

# 日
print(pd.date_range('1/1/2011', periods=5))

# 月
print(pd.date_range('1/1/2011', periods=5, freq='M'))
