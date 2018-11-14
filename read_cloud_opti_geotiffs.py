# -*- coding: utf-8 -*-
"""
read_cloud_opti_geotiffs.py

Created on Wed Nov 14 15:05:23 2018

@author: cscuser
"""


import rasterio
import matplotlib.pyplot as plt
import numpy as np
from rasterio.plot import show

# Specify the path for Landsat TIF on AWS
url = 'http://landsat-pds.s3.amazonaws.com/c1/L8/042/034/LC08_L1TP_042034_20170616_20170629_01_T1/LC08_L1TP_042034_20170616_20170629_01_T1_B4.TIF'

# Get the profile
src = rasterio.open(url)
# See the profile
#with rasterio.open(url) as src:
 #   print(src.profile)
 
 # Get the lis overviews
 oviews = src.overviews(1)
 oview = oviews[-1] 
oview

# Read a thumbnail using low resolution seource
  thumbnail = src.read(1, out_shape=(1, int(src.height // oview), int(src.width // oview)))
  
  # plot
  show(thumbnail, cmap="terrain")

# Retrieve a "Window" (a subset) from full resolution raster
  window = rasterio.windows.Window(1024, 1024, 1280, 2560)

# Retrieve a subset of the data
  subset = src.read(1, window=window)
