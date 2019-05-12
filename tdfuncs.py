# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 20:26:34 2017

Library of useful Thermodynamic Functions used in Atmospheric Sciences

Author: Jason A. Sulskis
Requires: phycon.py

"""
import numpy as np

# Call useful TD variables.
from phycon import phycon

# instantiate phycon object
phycon = phycon()

# Function to calculate the saturation vapor pressure. T is in K.
def es(T):

    # Return saturation vapor pressure
    return phycon.eso*np.exp(((phycon.Lvo+(phycon.Cl-phycon.Cpv)*phycon.Tko)/
                                phycon.Rv)*((1.0/phycon.Tko)-(10.0/T))-
    ((phycon.Cl-phycon.Cpv)/phycon.Rv)*np.log(T/phycon.Tko))
    
# Function to calculate the saturation vapor pressure of LW. T is in K.
def bolton(T):
    T = T - phycon.Tko
    return 6.1121*np.exp((17.67*T)/(T+243.5))

# Function to calculate the saturation vapor pressure of LW. T is in K.
def buck_water(T):
    T = T - phycon.Tko
    
    x = 18.678-(T/234.5)
    y = T/(257.14+T)
    
    return 6.1121*np.exp(x*y)

# Function to calculate the saturation vapor pressure of ice. T is in K.
def buck_ice(T):
    T = T - phycon.Tko
    
    x = 23.036-(T/337.7)
    y = T/(279.82+T)
    
    return 6.1115*np.exp(x*y)

# Function to calculate the latent heat of vaporization. T is in K. 
def lv(T):
    # Return Latent Heat of Vaporization
    return phycon.Lvo - (phycon.Cl - phycon.Cpv)*(T-phycon.Tko)

# Function to calculate the latent heat of vaporization. T is in K, P in Pa.
def ws(T, P):
    # Return mixing ratio
    return (phycon.epsilon)*es(T)/(P-es(T))

# Function to calculate the Function to determine the Saturated Adabatic Lapse
# Rate. T is in K, P in Pa.
def gamma_s(T, P):
    gamma_d = 0.0098 # Dry adiabatic lapse rate = 9.8 K/km = 0.0098 K/m
    
    L=lv(T)  # Get latent heat of vaporization
    w=ws(T,P)  # Get mixing ratio
    
    # Break expression up into parts to avoid mistakes with ()
    x1 = L*w
    x2 = phycon.Rd*T
    x = x1/x2
    y1 = phycon.epsilon*L**2.0*w
    y2 = phycon.Cpd*phycon.Rd*T**2.0
    y = y1/y2
    
    # Return value of gamma_s
    return gamma_d*((1.0+x)/(1.0+y))

# Function to determine the Potential Temperature. T is in K, P in Pa.
def theta(T, P):
    # Return Potential Temperature
    return T*(phycon.Po/P)**(phycon.Rd/phycon.Cpd) 

# Function to determine the Equiv. Potential Temperature. T is in K, P in Pa.
def theta_E(T, P):
    # Return Equivalent Potential Temperature
    return theta(T, P)*np.exp((phycon.Lvo*ws(T, P)/(phycon.Cpd*T)))

# Function to determine the LWC lapse rate. T is in K, P in Pa.
def gamma_l(T, P):
    H = 8500. # Assumed average scale height of 8.5 km
    
    gamma = gamma_s(T, P) # Get saturated adiabatic lapse rate (in K/m)
    
    L=lv(T)  # Get latent heat of vaporization
    w=ws(T,P)  # Get mixing ratio
    
    Pd=P-es(T)  # Calculate dry air pressure
    
    # Break expression up into parts to avoid mistakes with ()
    x1=(phycon.epsilon+w)*w*L
    x2=phycon.Rd*T**2.0
    x=x1/x2
    y1=w*P
    y2=Pd*H
    y=y1/y2
    
    # Return value of gamma_l
    return (gamma*x)-y
