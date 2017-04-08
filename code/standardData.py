# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 21:13:52 2017

@author: User
"""

import pandas as pd

filename='../data/wc_day57_69_avg.xlsx'
standardFile='../data/tmp/standard.xlsx'

data=pd.read_excel(filename,header=None)
data=(data-data.min())/(data.max()-data.min())# 标准化

data.to_excel(standardFile,index=False,header=False) #保存结果


