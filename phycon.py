# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 13:43:36 2017
@author: jsulskis
Useful constants for spectral and atmospheric physics.
Where avaliable, current NIST values are used. SI units.
"""

import math
import numpy as np

class phycon:
       
    def __init__(self):

        self.Tko = np.float64(273.15)                      # K
        self.Po = np.float64(1.0e+5)                       # Pa
        self.Rstar = np.float64(8.3144621)                 # J mol^-1 K^-1
        self.Rd = np.float64(287.05)                       # J K^-1 kg^-1
        self.Rv = np.float64(461.51)                       # J K^-1 kg^-1
        self.epsilon = self.Rd/self.Rv                     # unitless
        self.Cpd = np.float64(1005.2)                      # J K^-1 kg^-1
        self.Cvd = np.float64(719.0)                       # J K^-1 kg^-1
        self.Cpv = np.float64(1870.4)                      # J K^-1 kg^-1
        self.Cvv = np.float64(1410.0)                      # J K^-1 kg^-1
        self.Cl = np.float64(4218.0)                       # J K^-1 kg^-1
        self.Ci = np.float64(2106.0)                       # J K^-1 kg^-1
        self.Lvo = np.float64(2.5008e+6)                   # J kg^-1
        self.Lso =  np.float64(2.8345e+6)                  # J kg^-1
        self.rhol = np.float64(1000.0)                     # kg m^-3
        self.rhoi = np.float64(917.0)                      # kg m^-3
        self.eso = np.float64(610.7)                       # J kg^-1
        self.g = np.float64(9.81)                          # m s^-2
        self.G = np.float64(6.67e-11)                      # N m^2 kg^-2
        self.c = np.float64(2.99792458e+8)                 # m s^-1
        self.h = np.float64(6.626068963e-34)               # W s^2
        self.kB = np.float64(1.3806504e-23)                # W s K^-1
        self.c1 = 2*math.pi*self.h*self.c**2               # W m^2 sr^-1
        self.c2 = self.h*self.c/self.kB                    # m K
        self.Gammad = self.g/self.Cpd                      # K m^-1
        self.Kappa = np.float64(2.40e-1)                   # J m^-1 s^-1 K^-1
        self.sigmaT = np.float64(5.670367e-8)              # W m^-2 K^-4
        self.a = 6.378137e6                                # m
        self.b = 6.3567523142e6                            # m
        self.f = 1/298.257223563                           # unitless
