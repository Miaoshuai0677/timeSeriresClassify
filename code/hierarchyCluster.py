# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 21:40:19 2017

@author: User
"""

import pandas as pd
standardFile='../data/tmp/standard.xlsx'
k=4
data=pd.read_excel(standardFile,header=None)

from sklearn.cluster import AgglomerativeClustering

model =AgglomerativeClustering(n_clusters=k,linkage='ward')
model.fit(data)

r= pd.concat([data,pd.Series(model.labels_)],axis=1)
r.columns=list(data.columns)+[u'cluster class']


