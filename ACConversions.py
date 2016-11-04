# -*- coding: utf-8 -*-
"""

Useful Conversions for Aircraft Research
Created on Thu Nov  3 15:50:42 2016

@author: jsulskis
@requires geopy

Make sure ACCoversions.py is in your PYTHONPATH !!

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
import numpy as np
from geopy.distance import great_circle

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

""" Calculate list of Slant Ranges """
def CalculateSlantRanges(data, survey = [np.nan,np.nan]):
    
    lat = survey[0]
    lon = survey[1]
    if len(survey) > 2:
        alt = survey[2]
    else:
        alt = 0.0

    ranges = []
    for row in data.itertuples():
        ranges.append(math.sqrt((great_circle((row[1],row[2]), (lat,lon)).meters)**2 + ((row[3]*0.3048)-alt)**2))
        
    return ranges