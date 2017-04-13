# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 13:43:36 2017

@author: jsulskis

Useful constants for spectral and atmospheric physics.

Where avaliable, current NIST values are used. SI units.

"""

import math
import numpy as np

Tko = np.float64(273.15) # K
Po = np.float64(1.0e+5) # Pa
Rstar = np.float64(8.3144621) # J mol^-1 K^-1
Rd = np.float64(287.05) # J K^-1 kg^-1
Rv = np.float64(461.51) # J K^-1 kg^-1
epsilon = Rd/Rv # unitless
Cpd = np.float64(1005.2) # J K^-1 kg^-1
Cvd = np.float64(719.0) # J K^-1 kg^-1
Cpv = np.float64(1870.4) # J K^-1 kg^-1
Cvv = np.float64(1410.0) # J K^-1 kg^-1
Cl = np.float64(4218.0) # J K^-1 kg^-1
Ci = np.float64(2106.0) # J K^-1 kg^-1
Lvo = np.float64(2.5008e+6) # J kg^-1
Lso =  np.float64(2.8345e+6) # J kg^-1
rhol = np.float64(1000.0) # kg m^-3
rhoi = np.float64(917.0) # kg m^-3
eso = np.float64(610.7) # J kg^-1
g = np.float64(9.81) # m s^-2
G = np.float64(6.67e-11) # N m^2 kg^-2
c = np.float64(2.99792458e+8) # m s^-1
h = np.float64(6.626068963e-34) # W s^2
kB = np.float64(1.3806504e-23) # W s K^-1
c1 = 2*math.pi*h*c**2 # W m^2 sr^-1
c2 = h*c/kB # m K
Gammad = g/Cpd #K m^-1
Kappa = np.float64(2.40e-1) # J m^-1 s^-1 K^-1