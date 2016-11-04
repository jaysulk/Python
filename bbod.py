# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 14:17:44 2016

@author: jsulskis

 BBOD Calculates the spectral irradiance for a black body
 based on Max Planck's law in pW/cm^2 for an inputted bandpass
    
     [] = BBOD(L1, L2, TEMP) computes the spectral irradiance 
     based on Planck's law based for a given temperature 
     (TEMP, in Kelvin) and wavelength band (L1,2 in micro meter [10^-6 m]) 
  
     The function does not exist for L1,2 == 0 or for T <= 0.  
  
     Values of constants are taken from current NIST values.
     
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

import math
from scipy import integrate

def bbod(l1,l2, T):
    
    # Speed of light in a vacuum (NIST)
    c = 2.99792458e+8 # m/s 
    
    # Planck's constant (NIST)
    h = 6.626068963e-34 # W s^2 
    
    # Boltzman constant (NIST)
    k = 1.3806504e-23 # W s/K
    
    # First Radiation constant for spectral radiance:
    c1 = 2*math.pi*h*c**2 
    
    # Second Radiation constant:
    c2 = h*c/k 

    if T < 0:
         print 'Input Temperature Less Than Zero!'
         return
       
    if T > 0:
        
        # Spectral Irradiance
        SpectralIrradiance, error = integrate.quad(lambda x: c1*x**(-5)/(math.exp((c2/T)/x)-1),l1,l2)
        SpectralIrradiance = SpectralIrradiance*0.0001
        SpectralIrradiance = SpectralIrradiance/1e-12
    
    return SpectralIrradiance
