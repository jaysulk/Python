# -*- coding: utf-8 -*-
"""

Calculate end IRIG time given start time and duration
Created on Thu Nov  3 15:50:42 2016

@author: jsulskis
@requires IRIGConversions

(c) 2016 Jason A. Sulskis

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

import pandas as pd
import numpy as np

from IRIGConversions import IrigToSec, SecToIrigStr

# CalculateStopIrig - Compute stop IRIG based on start IRIG and duration.
def CalculateStopIrig(irigFile):

# Vectorized lambda function to convert IRIG times
    conv = np.vectorize(lambda x: IrigToSec(x) if(not pd.isnull(x)) else x)
   
    # Read in raw data to pandas dataframe
    df = pd.read_csv(irigFile, sep='\t')
    
    # parse IRIG times
    t1 = np.array(conv(df.ix[:,0]))
    dur = np.array(df.ix[:,1])
   
    # compute end time
    t2 = t1 + dur
    
    # compute end time strig
    stopIrig = SecToIrigStr(t2)
    
    print("\n".join(stopIrig))
    
    
    
