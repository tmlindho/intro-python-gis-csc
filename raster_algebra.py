# -*- coding: utf-8 -*-
"""
raster_algebra.py

How to do raster calculations using rasterio and numpy

Created on Wed Nov 14 12:59:05 2018

@author: cscuser
"""

import rasterio
import numpy as np
from rasterio.plot import show
import os
import matplotlib.pyplot as plt
%matplotlib inline

# Data dir
data_dir = "L5_data"

# Filepath
fp = os.path.join(data_dir, "Helsinki_masked.tif")

# Open the raster file in read mode
raster = rasterio.open(fp)

# Read red channel (channel number 3)
red = raster.read(3)
# Read NIR channel (channel number 4)
nir = raster.read(4)

# Calculate some stats to check the data
print(red.mean())
print(nir.mean())
print(type(nir))

# Visualize
show(nir, cmap='terrain')

# Convert to floats
red.dtype
red = red.astype("f4")
nir = nir.astype("f4")
nir.dtype

# Ignore division by zero exception
np.seterr(divide='ignore', invalid='ignore')

# Calculate NDVI
ndvi = ((nir-red)/(nir+red))

# Plot NDVI with Legend
# r changes the color vice versa
plt.imshow(ndvi, cmap="terrain_r")
plt.colorbar()

# Time series, dimensions of the data has to be the same
# See geohackweek.github.io
change = year2018 - year2008