# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 17:21:15 2016

@author: jsulskis

Adapted from:

http://stackoverflow.com/questions/30493614/pandas-merge-dataframes-based-on-closest-match/30494118

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
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