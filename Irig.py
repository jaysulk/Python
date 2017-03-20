# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 12:24:28 2017

@author: jsulskis
"""
from datetime import datetime
import astropy.time, math

class Irig:
    
    def __init__(self,d = 1,h = 0,m = 0,s = 0,u = 0):
        self.day = d
        self.hour = h
        self.minute = m
        self.second = s
        self.millisecond = u
    
    def string(self):
        return '{:003d}:{:02d}:{:02d}:{:06.3f}'.format(self.day,self.hour,self.minute,self.second,self.millisecond)

    def seconds(self):
        
        return self.day*24.0*60.0*60.0 + self.hour*60.0*60.0 + self.minute*60.0 + self.second + self.millisecond/1000.0
        
    def jd(self, year):
        
        JD = astropy.time.Time(datetime(year,1,1,0,0,0,0)).jd
        JCD = self.day + 0.5
        return JD + JCD - 1
        
    def datetime(self, year):
        
        JD = self.jd(year)
        
        H = self.hour
        M = self.minute
        S = self.second
        MS = self.millisecond*1000.0
        
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