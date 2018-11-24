#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
from scipy import misc
import os
import numpy as np 
import cv2

""" Returns a list of filenames for all images in directory with given extension 'ext' """
def get_imList(path, ext):
	return [os.path.join(path,f) for f in os.listdir(path) if f.endswith(ext)]

def compute_std(image):
    
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    x, y = img.shape[:2]
    avg = np.std(img)
    print(image)
    print(str(x) + ", " + str(y) + ", " + str(avg))
    
    return avg
        
def main():

    path = os.getcwd()
    images = get_imList(path, '.bmp')
    
    for image in images:
        avg = compute_std(image)
        
main()