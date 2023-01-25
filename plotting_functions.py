# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 16:03:34 2019

@author: chowe7
"""
# to do: add stim times function


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors
import pylab as P
from datetime import date
import matplotlib.cm as cm
import scipy.ndimage as ndimage

font = {'family': 'sans',
        'weight': 'normal',
        'size': 18,}

plt.rc('font',**font)    
    

def saveFigure(fig,path,keyword):
    plt.savefig(path + r'\\{}.png'.format(keyword), format='png', dpi=600, bbox_inches='tight')
    plt.savefig(path + r'\\{}.eps'.format(keyword), format='eps', dpi=1900, bbox_inches='tight')
    plt.close(fig)   
    return


def saveFigurePNG(fig,path,keyword):
    plt.savefig(path + r'\\{}.png'.format(keyword), format='png', dpi=600, bbox_inches='tight')
    plt.close(fig)   
    return


def plotImageScaleBar(fig,xS,lengthSB,pixelSize,y):
#    xS=12
#    lengthSB = 25
#    y = 17
#    
#    fig = plt.gcf()      
#    ax = plt.subplot(111)  
#    plt.imshow(result[40,48:68,42:62])
    plt.plot([xS,xS+(lengthSB/pixelSize)],[y,y],linewidth=6.0,color='w')
    return 


def to_outline(roi):
    return np.logical_xor(ndimage.morphology.binary_dilation(roi),roi)


def addROI(image,outline):
    my_cmap = cm.hsv
    my_cmap.set_under('k', alpha=0)
    fig, ax = plt.subplots()
    ax.imshow(image, cmap=cm.viridis)
    ax.imshow(outline*1, cmap=cm.hsv, interpolation='none',clim=[0.9, 1])
    return fig,ax

def plotTimeData_noAxis(ts, trace,xS,xE,yS,yE):
    time = np.arange(0, ts*len(trace), ts)

    fig = plt.gcf()      
    ax = plt.subplot(111)  
    plt.plot(time,trace,linewidth=3.0,color='k')
    plt.plot([xS,xS],[yS,yE],linewidth=4.0,color='k')
    plt.plot([xS,xE],[yS,yS],linewidth=4.0,color='k')
    fig.set_size_inches(8,4)
    
    #axis formatting
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_linewidth(False)
    ax.spines['left'].set_linewidth(False)
    ax.axes.get_yaxis().set_ticks([])
    ax.axes.get_xaxis().set_ticks([]) 
    return
 
def squarePlot(ax):
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    return ax

def plotRect_withAxis(y,ts): 
    time = np.arange(0, ts*len(y), ts)    
    
    fig = plt.gcf()      
    ax = plt.subplot(111)  
    plt.plot(time,y,linewidth=2.0,color='k')
    fig.set_size_inches(8,4)
    
    #axis formatting
    ax.spines['right'].set_visible(False)
    ax.spines['figtop'].set_visible(False)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
      
    return fig


def plotTimeData_noAxis_withStim(ts,processedTrace,stimIndices,xS,xE,yS,yE):
    time = np.arange(0, ts*len(processedTrace), ts)
    stimTimes = stimIndices*ts

    fig = plt.gcf()      
    ax = plt.subplot(111)  
    plt.plot(time,processedTrace,linewidth=3.0,color='k')
    plt.plot([xS,xS],[yS,yE],linewidth=4.0,color='k')
    plt.plot([xS,xE],[yS,yS],linewidth=4.0,color='k')
    plt.plot([stimTimes,stimTimes],[0,0.001])
    fig.set_size_inches(8,4)
    
    #axis formatting
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_linewidth(False)
    ax.spines['left'].set_linewidth(False)
    ax.axes.get_yaxis().set_ticks([])
    ax.axes.get_xaxis().set_ticks([])
       
    return fig


def make_square_plot(ax):
    ax.set_aspect(np.diff(ax.get_xlim())/np.diff(ax.get_ylim()),adjustable = 'box')
    return
    
    
def plotSquareFig(x,y):
    plt.rc('font',**font)
    fig = plt.gcf()      
    ax = plt.subplot(111)
    plt.plot()  
    plt.plot(x,y,linewidth=2.5,color='k')
    
    #axis formatting
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)

    #plt.legend(legend, loc='upper right', frameon=False, bbox_to_anchor=(1,1.0))
    plt.xlabel('Distance (um)', fontdict = font)
    plt.ylabel('Intensity (a.u.)', fontdict = font)
    plt.tight_layout()
    
    return fig    


def forceAspect(ax,aspect=1):
    im = ax.get_images()
    extent =  im[0].get_extent()
    ax.set_aspect(abs((extent[1]-extent[0])/(extent[3]-extent[2]))/aspect)
    return


def noBorders(ax):
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_linewidth(False)
    ax.spines['left'].set_linewidth(False)
    ax.axes.get_yaxis().set_ticks([])
    ax.axes.get_xaxis().set_ticks([]) 
    return


def lrBorders(ax):
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    return


def plotImage(image):
    fig = plt.gcf()      
    ax = plt.subplot(111)  
    plt.imshow(image)
       
    #axis formatting
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_linewidth(False)
    ax.spines['left'].set_linewidth(False)
    ax.axes.get_yaxis().set_ticks([])
    ax.axes.get_xaxis().set_ticks([]) 
    forceAspect(ax,aspect=1)
    plt.tight_layout()  
    return fig


def plotLogImage(image):
    fig = plt.gcf()      
    ax = plt.subplot(111)  
    plt.imshow(image,norm=colors.LogNorm(vmin=image.min(), vmax=image.max()))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_linewidth(False)
    ax.spines['left'].set_linewidth(False)
    ax.axes.get_yaxis().set_ticks([])
    ax.axes.get_xaxis().set_ticks([]) 
    forceAspect(ax,aspect=1)
    plt.tight_layout()  
    plt.colorbar()
    
    return fig
    
def boxPlot(data,y_axisLabel):
    boxprops = dict(linewidth=2)
    medianprops = dict(linewidth=2.5,color='DarkCyan')
    flierprops = dict(markersize=10,linestyle='none')
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    bp=plt.boxplot(data,boxprops=boxprops,medianprops=medianprops,flierprops=flierprops)
    my_xticks = ['Widefield', 'Refoc.', 'Deconv.']
    x=np.array([1,2,3])
    plt.xticks(x, my_xticks)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    plt.ylabel('{}'.format(y_axisLabel), fontdict = font)
   # plt.xlim((0.5,3.1))
    plt.tight_layout()
    
    for whisker in bp['whiskers']:
        whisker.set(linewidth=3)
    for cap in bp['caps']:
        cap.set(linewidth=3)
    return fig
    
def boxPlotMarkers(data):
    for i in range(len(data)):
        y = data[i]
        x = np.random.normal(1+i, 0.04, size=len(y))
        P.plot(x, y, 'r.', markersize=14, alpha=0.6)
    return


def sigBars(plotting,para):
    plt.plot([1, 2], [round(plotting.para.max(),ndigits=-1),round(plotting.para.max(),ndigits=-1)],linewidth=3.0,color='k')
    plt.plot([2, 3], [round(plotting.para.max(),ndigits=-1)+5,round(plotting.para.max(),ndigits=-1)+5],linewidth=3.0,color='k')
    plt.plot([1, 3], [round(plotting.para.max(),ndigits=-1)+10,round(plotting.para.max(),ndigits=-1)+10],linewidth=3.0,color='k')
    
    plt.plot([1, 1], [round(plotting.para.max(),ndigits=-1)-1,round(plotting.para.max(),ndigits=-1)],linewidth=3.0,color='k')
    plt.plot([2, 2], [round(plotting.para.max(),ndigits=-1)-1,round(plotting.para.max(),ndigits=-1)],linewidth=3.0,color='k')
    plt.plot([2, 2], [round(plotting.para.max(),ndigits=-1)+4,round(plotting.para.max(),ndigits=-1)+5],linewidth=3.0,color='k')
    plt.plot([3, 3], [round(plotting.para.max(),ndigits=-1)+4,round(plotting.para.max(),ndigits=-1)+5],linewidth=3.0,color='k')
    plt.plot([1, 1], [round(plotting.para.max(),ndigits=-1)+9,round(plotting.para.max(),ndigits=-1)+10],linewidth=3.0,color='k')
    plt.plot([3, 3], [round(plotting.para.max(),ndigits=-1)+9,round(plotting.para.max(),ndigits=-1)+10],linewidth=3.0,color='k')
    return
