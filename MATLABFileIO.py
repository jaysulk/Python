# -*- coding: utf-8 -*-
"""

MATLAB-like file I/O functions
Created on Thu Nov  3 15:50:42 2016

@author: jsulskis

Make sure MATLABFileIO.py is in your PYTHONPATH !!

"""

import numpy as np


def fread(fileID, sizeA, precision):
   # Datatype conversions
   dtype = {'uint8': np.uint8, 'uint16':np.uint16, 'uint32':np.uint32,
            'uint64':np.uint64, 'int8': np.int8, 'int16':np.int16,
            'int32':np.int32, 'float':np.float32, 'double':np.float64,
            'single':np.float32, 'char': np.uint8, 'short': np.float16}

   # Read in numpy array from open file
   data = np.fromfile(fileID, dtype[precision], sizeA)

   # convert numpy array to a list
   data = data.tolist()

   # return list
   return data

def fseek(fileID, offset, origin):
    # determine where in file to seek from
    if origin is 'bof':
        whence = 0
    elif origin is 'cof':
        whence = 1
    elif origin is 'eof':
        whence = 2

    # seek to desired position
    fileID.seek(offset, whence)

def ftell(fileID):
    # return tell
    return fileID.tell()

