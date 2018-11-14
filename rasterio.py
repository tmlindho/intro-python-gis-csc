# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 09:02:35 2018

rasterio.py

Reading raster files with rasterio

@author: cscuser
"""

import rasterio 
import os
import numpy as np

# Data, r means that don't intepret anything, like n\ means new line and t\ is tabulator
# os.path.join merges the paths together
data_dir = r"C:\IntroGIS"
fp = os.path.join(data_dir, "L5_data", "Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif")

# Open the file

# Open the file:
raster = rasterio.open(fp)

# Check type of the variable 'raster'
type(raster)
# Projection
raster.crs
# Affine transform (how raster is scaled, rotated, skewed, and/or translated)
raster.transform
# Dimensions
print(raster.width)
print(raster.height)

# Number of bands
raster.count

# Bounds of the file
raster.bounds
# Driver (data format)
raster.driver
# No data values for all channels
raster.nodatavals
# All Metadata for the whole raster dataset
raster.meta

# Read the raster band as separate variable
band1 = raster.read(1)

# Check type of the variable 'band'
print(type(band1))

# Data type of the values
print(band1.dtype)

# Read all bands
array = raster.read()

# Calculate statistics for each band. Again there's something wrong here
stats = []

  stats = []
for band in array:
    stats.append({
        'min': band.min(),
        'mean': band.mean(),
        'median': np.median(band),
        'max': band.max()})
  
    for idx, band in enumerate(array):
    band_stat = {
        'min': band.min(),
        'mean': band.mean(),
        'median': np.median(band),
        'max': band.max()}
  
    # Insert stats inside another dict So you can manipulate the values of each band
    channel_stat = {"channel %s" % idx+1: band_stat}

# Show stats for each channel
stats






