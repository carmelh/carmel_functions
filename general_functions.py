# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 15:52:45 2019

@author: chowe7
"""

import numpy as np
import scipy.ndimage as ndimage
import scipy.constants
import csv
import read_roi as rr

#if __name__ =='__main__':
 #   import read_roi as rr
#else:
 #   from . import read_roi as rr


def importCSV(cwd,filename):
    x=[]
    y=[]
    with open(cwd + r'{}.csv'.format(filename), newline='') as csvfile:
        file= csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in file:
        x.append(float(row[0]))
        y.append(float(row[1]))  
    return x,y

def two_photon_res(wl,NA):
    return (0.383*wl)/NA**0.91

def power_to_photon_flux(wl,power,NA = 0.8):
    spot_area = 2*np.pi*two_photon_res(wl,NA)**2
    photon_flux = power*(wl/(scipy.constants.h*scipy.constants.c))
    flux_density = photon_flux/spot_area
    return flux_density

def norm(array):
    return [float(i)/max(array) for i in array]
    #(array - np.min(array))/(np.max(array) - np.min(array))
    
def read_roi_file(roi_filepath,im_dims = None):
    with open(roi_filepath,'rb') as f:
        roi = rr.read_roi(f)
    
    if im_dims is not None:
        im = np.zeros(im_dims)
        for pair in roi:
            im[pair[0],pair[1]] = 1            
        clos = ndimage.binary_dilation(im,iterations = 1)
        filled = ndimage.binary_fill_holes(clos)
        filled = ndimage.binary_erosion(filled)
        return roi,filled
    else:
        return roi