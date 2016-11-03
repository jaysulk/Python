# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 17:21:15 2016

@author: jsulskis
"""

import numpy as np
import pandas as pd

def MatchTime(df1, df2):
    
    # Match to closest times
    edges, labels = np.unique(df2['Time'], return_index=True)
    edges = np.r_[-np.inf, edges + np.ediff1d(edges, to_end=np.inf)/2]
    df1['x'] = pd.cut(df1['Time'], bins=edges, labels=df2.index[labels])
    output = df1.join(df2, on='x', rsuffix='_b')
    
    return output