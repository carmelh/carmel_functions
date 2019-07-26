# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 16:03:34 2019

@author: chowe7
"""
import csv
import matplotlib.pyplot as plt
import numpy as np

def plotTimeData(ts, processedTrace,xS,xE,yS,yE,path):
    font = {'family': 'sans',
            'weight': 'normal',
            'size': 16,}
    
    plt.rc('font',**font)
    
    time = np.arange(0, ts*len(processedTrace), ts)

    fig = plt.gcf()      
    ax = plt.subplot(111)  
    plt.plot(time,processedTrace,linewidth=3.0,color='k')
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
    plt.savefig(path + r'\\figure_{}.png'.format(keyword), format='png', dpi=600)
    plt.savefig(path + r'\\figure_{}.eps'.format(keyword), format='eps', dpi=1000)
    
    return
    

def make_square_plot(ax):
    ax.set_aspect(np.diff(ax.get_xlim())/np.diff(ax.get_ylim()),adjustable = 'box')
    
    
def plotSquareFig(x,y,path):
    font = {'family': 'sans',
        'weight': 'normal',
        'size': 16,}
    
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
    plt.savefig(path + r'\\figure.png', format='png', dpi=600)
    plt.savefig(path + r'\\figure.eps', format='eps', dpi=1000)

    return    