#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
from scipy import misc
import os
import numpy as np 
import cv2
from matplotlib import pyplot as plt
import sys

DBL_MIN = sys.float_info.min

""" Returns a list of filenames for all images in directory with given extension 'ext' """
def get_imList(path, ext):
	return [os.path.join(path,f) for f in os.listdir(path) if f.endswith(ext)]

# calculate standard deviation
def compute_std(image):
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    x, y = img.shape[:2]
    std = np.std(img)
    #print(image + ", " + str(x) + ", " + str(y) + ", " + str(std))
    return std
    
# the ratio of the average signal value to the standard deviation of the signal
def compute_snr(image):
    
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    x, y = img.shape[:2]
    snr = 0
    
    # thresholding to detect letters
    avg = np.mean(img)
    ret,thresh = cv2.threshold(img,avg,255,cv2.THRESH_TOZERO)
    #misc.imsave(image + "2.bmp", thresh)
    
    # calculate avg of signal (where pixel is not zero)
    signal_avg = np.nanmean(np.where(np.isclose(thresh,0), np.nan, thresh))
    # calculate std of signal (where pixel is not zero)
    signal_std = np.nanstd(np.where(np.isclose(thresh,0), np.nan, thresh))
    tot_int = np.nansum(np.where(np.isclose(thresh,0), np.nan, thresh))
    snr = signal_avg / signal_std
    return snr, signal_avg, tot_int

# compute image integral    
def compute_integral(image):
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    integral = cv2.integral(img)
    return integral
        
# calculate summed intensity of the image
def cumulated_intensity(image):
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    intensity = np.sum(img)
    return intensity
        
def main():

    path = os.getcwd()
    images = get_imList(path, '.bmp')
    
    for image in images:
        snr, avg_int, tot_int = compute_snr(image)
        std = compute_std(image)
        #integral = compute_integral(image)
        #intensity = cumulated_intensity(image)
        print(os.path.basename(image) + ", " \
        + str(std) + ", " \
        + str(snr) + ", " \
        + str(tot_int) + ", " \
        + str(avg_int))
        
        
main()