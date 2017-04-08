# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 21:33:00 2017

@author: User
"""

import pandas as pd
standardFile='../data/tmp/standard.xlsx'
data=pd.read_excel(standardFile,header=None)

import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

z=linkage(data,method='ward',metric='euclidean')
p=dendrogram(z,0)
plt.show()