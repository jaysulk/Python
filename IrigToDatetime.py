# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:33:32 2017

@author: jsulskis
@requires: astropy

adapted from https://gist.github.com/jiffyclub/1294443

(c) 2017 Jason A. Sulskis & Matt Davis

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
from datetime import datetime
import astropy.time, math

def IrigToDatetime(year,irig):
    
    if isinstance(irig, str):
        
        JD = astropy.time.Time(datetime(year,1,1,0,0,0,0)).jd
   
        JCD = float(irig[0:3]) + 0.5
        JD = JD + JCD - 1
        H = float(irig[4:6])
        M = float(irig[7:9])
        S = float(irig[10:12])
        MS = float(irig[13:])*1000.0
        
        F, I = math.modf(JD)
        I = int(I)
        A = math.trunc((I - 1867216.25)/36524.25) 
        if I > 2299160:
            B = I + 1 + A - math.trunc(A / 4.)
        else:
            B = I     
        C = B + 1524  
        D = math.trunc((C - 122.1) / 365.25) 
        E = math.trunc(365.25 * D)  
        G = math.trunc((C - E) / 30.6001)  
        day = C - E + F - math.trunc(30.6001 * G) 
        if G < 13.5:
            month = G - 1
        else:
            month = G - 13       
        if month > 2.5:
            year = D - 4716
        else:
            year = D - 4715

        return datetime(int(year), int(month), int(day), int(H), int(M), int(S), int(MS))
    
    else:
    
        return