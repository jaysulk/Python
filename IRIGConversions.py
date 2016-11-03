# -*- coding: utf-8 -*-
"""

Useful Conversions for standard IRIG time stamps
Created on Thu Nov  3 15:50:42 2016

@author: jsulskis

Make sure IRIGConversions.py is in your PYTHONPATH !!

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

