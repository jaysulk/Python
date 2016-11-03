# -*- coding: utf-8 -*-
"""

Useful Conversions for Aircraft Research
Created on Thu Nov  3 15:50:42 2016

@author: jsulskis

Make sure MATLABFileIO.py is in your PYTHONPATH !!

"""

import math
import numpy as np

""" Convert from NED to Aircraft Coordinates """
def NedToAircraft(azNed, elNed, roll, pitch, yaw):

    # compute rotation matrix from earth to a/c coordinate system
    My = np.array([[math.cos(math.radians(yaw)), -math.sin(math.radians(yaw)), 0],[math.sin(math.radians(yaw)), math.cos(math.radians(yaw)), 0],[0, 0, 1]])
    Mp = np.array([[math.cos(math.radians(pitch)), 0, math.sin(math.radians(pitch))],[0, 1, 0],[-math.sin(math.radians(pitch)), 0, math.cos(math.radians(pitch))]])
    Mr = np.array([[1, 0, 0],[0, math.cos(math.radians(roll)), -math.sin(math.radians(roll))],[0, math.sin(math.radians(roll)), math.cos(math.radians(roll))]])
    M = np.transpose(My.dot(Mp).dot(Mr))

    # compute NED directional vector
    dNed = np.array([[math.cos(math.radians(elNed))*math.cos(math.radians(azNed))], [math.cos(math.radians(elNed))*math.sin(math.radians(azNed))], [-math.sin(math.radians(elNed))]])

    # compute ac directional vector
    dAc = np.dot(M,dNed)

    # compute az and el in aircraft coordinates
    azAc = round(math.degrees(math.atan2(dAc[1], dAc[0])),1)
    elAc = round(math.degrees(-math.asin(dAc[2])),1)

    return azAc, elAc

