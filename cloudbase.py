# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 09:01:12 2017

@author: Jason
"""
import numpy as np
import phycon
import tdfuncs

# Function to determine the lifted condensation level using a "Skew-T method"
# Tf/Tdf is in C, Pf in hPa.
def cloudbase(Tf,Tdf,Pf):
    # Define Arrays
    T=(np.arange(801)*0.1)-30 # Create T array
    TK=T+phycon.Tko # Convert from degrees C to K
    P=np.arange(801)+250 # Create P array
    P=P[::-1]  # Reverse P array so Higher pressure is first &
    PA = P*100.0  # convert to Pa
    Es = tdfuncs.es(TK)  # Define Saturation Vapour Pressure
    
    PP = (1e5/PA)**(phycon.Rd/phycon.Cpd) 
    
    # Define Potential Temperature
    theta = np.outer(TK,PP)
     
    # Define Saturation Mixing Ratio in g/kg
    Ws = np.empty((TK.size,PP.size))
    for idx, line in enumerate(Ws):
        Ws[:,idx] = 1000*phycon.epsilon*Es[:]/(PA[idx]-Es[:])
      
    # Define Equivalent Potential Temperature
    thetaE = np.empty((TK.size,PP.size))
    for idx, line in enumerate(thetaE):
        thetaE[idx,:] = theta[idx,:]*np.exp((phycon.Lvo*
              Ws[idx,:])/(phycon.Cpd*TK[idx]))
       
    # Calculate LCL
    indP = np.abs(P-Pf).argmin()
    indT = np.abs(T-Tf).argmin()
    indTd = np.abs(T-Tdf).argmin()
    theta0=theta[indT,indP]
    Wd=Ws[indTd,indP]
    WLCL=Ws[indT,indP]
    while Wd < WLCL:
        PLCL=P[indP]
        indTheta = np.abs(theta[:,indP]-theta0).argmin()
        thetaLCL=theta[indTheta,indP]
        thetaELCL=thetaE[indTheta,indP]
        TLCL=T[indTheta]
        WLCL=Ws[indTheta,indP]
        indP+=1
        
    # return parameters at cloud base
    return [PLCL,TLCL,WLCL,thetaLCL,thetaELCL]