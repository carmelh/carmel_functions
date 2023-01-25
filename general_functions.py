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
import pickle
from scipy import signal
from scipy.signal import find_peaks, peak_widths
from pathlib import Path
from scipy.interpolate import UnivariateSpline

#if __name__ =='__main__':
 #   import read_roi as rr
#else:
 #   from . import read_roi as rr

from time import perf_counter

#start = perf_counter()
#do thing
#end = perf_counter()
#execution_time = (end - start)
#print(execution_time)



def to_outline(roi):
    return np.logical_xor(ndimage.morphology.binary_dilation(roi),roi)

def importCSV(cwd,filename):
    x=[]
    y=[]
    with open(cwd + r'\\{}.csv'.format(filename), newline='') as csvfile:
        file= csv.reader(csvfile, delimiter=',')
        next(csvfile)
        for row in file:
            x.append(float(row[0]))
            y.append(float(row[1]))  
    return x,y


def appendCSV(cwd,fileName,data):
    with open(cwd + r'\{}.csv'.format(fileName), 'a', newline='') as f:
        writer = csv.writer(f, lineterminator='\r')
        writer.writerow(data)
    return
    

def savePickes(cwd,fileName,variableName):
    with open(cwd + '\\{}'.format(fileName), 'wb') as f:
        pickle.dump(variableName, f) 
    return


def loadPickles(cwd,fileName):
   with open(cwd + '\\{}'.format(fileName), 'rb') as f:
        variableName = pickle.load(f)
   return variableName
    

def makeFolder(path):
    path = Path(path)

    if not path.is_dir():
        path.mkdir()
    return

def countToPhotons(count):
    return count*100*2**16/30000
    


def two_photon_res(wl,NA):
    return (0.383*wl)/NA**0.91



def power_to_photon_flux(wl,power,NA = 0.8):
    spot_area = 2*np.pi*two_photon_res(wl,NA)**2
    photon_flux = power*(wl/(scipy.constants.h*scipy.constants.c))
    flux_density = photon_flux/spot_area
    return flux_density


def norm(array):
    return [float(i)/np.max(array) for i in array]
    #(array - np.min(array))/(np.max(array) - np.min(array))


def FWHM(x):
    peaks, _ = find_peaks(x, height=0)
    results_half = peak_widths(x, peaks, rel_height=0.5)
    return peaks, results_half

def FWHM2(x,y):
    spline = UnivariateSpline(x, y-np.max(y)/2, s=0)
    r1, r2 = spline.roots() # find the roots
    FWHM=r2-r1
    return FWHM

def get_time(ts,processedTrace):
    return np.arange(0, ts*len(processedTrace), ts)


def get_stats(data):
    med= np.median(data)
    tenth=np.percentile(data,10)
    ninieth=np.percentile(data,90)
    
    return med, tenth, ninieth   
    
    
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
    
def detrend(y):    
    return signal.detrend(y)    
