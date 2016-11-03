# -*- coding: utf-8 -*-
"""

Useful Conversions for standard IRIG time stamps
Created on Thu Nov  3 15:50:42 2016

@author: jsulskis

Make sure IRIGConversions.py is in your PYTHONPATH !!

"""

import numpy as np

""" Convert number of seconds to IRIG time dictionary """
def SecToIrig(sec):
    # initalize irig dictionary
    irig = {}

    # populate dictionary based on number of seconds
    day = np.floor(sec[0]/(24*60*60))
    sec = sec[0] - day*24.0*60.0*60.0
    hour = np.floor(sec/(60.0*60.0))
    sec = sec - hour*60.0*60.0
    mins = np.floor(sec/60.0)

    # append to ditionary
    irig['day'] = int(day)
    irig['hour'] = int(hour)
    irig['min'] = int(mins)
    irig['sec'] = float(sec - mins*60.0)

    # return irig time dictionary
    return irig

""" Convert time dictionary to seconds """
def IrigDictToSec(time):
    # convert IRIG time to seconds
    tSec = float(time['day'])*24*60*60 + float(time['hour'])*60*60 + float(time['min'])*60 + float(time['sec'])

    # return time in seconds
    return tSec

