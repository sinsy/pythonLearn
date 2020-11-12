#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import pandas as pd
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 设为基本路径
df = pd.read_csv(BASE_DIR+"/华测检测-财报对比图-20191025_173204.csv")
print(df)
