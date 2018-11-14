# -*- coding: utf-8 -*-
"""

visualize_raster.py

Visualizing raster data with rasterio

Created on Wed Nov 14 10:05:21 2018

@author: cscuser
"""

import rasterio
from rasterio.plot import show
from rasterio.plot import show_hist
import numpy as np
import os
import matplotlib.pyplot as plt

# Import normalize() function from raster_tools Python script
# This works as long as they are in the same directory
from raster_tools import normalize

#Filepath
data_dir = "L5_data"
fp = os.path.join(data_dir, "Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif")

# What is the filename of our raster
filename = os.path.basename(fp)
filename

#Open the file
raster = rasterio.open(fp)
raster

#Plot the channel 1
show((raster, 1))

#Plot the channel 3 in alternative manner
show(raster.read(3))

# Visualize channels 1, 2 and 3
# Sharey tells that we can have the same coordinates
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(10, 4), sharey=True)

# Plot
show((raster, 3), cmap="Reds", ax=ax1)
show((raster, 2), cmap="Greens", ax=ax2)
show((raster, 1), cmap="Blues", ax=ax3)

# Set titles
ax1.set_title("Red")
ax2.set_title("Green")
ax3.set_title("Blue")

# Create true color composite

#Read channels into numpy arrays

red = raster.read(3)
green = raster.read(2)
blue = raster.read(1)

# Normalize the bands. This function was imported, so you don't need to write the code several times
# And if you have a mistake you need to correct it only once
redn = normalize(red)
greenn = normalize(green)
bluen = normalize(blue)

# Create the composite
rgb = np.stack((redn, greenn, bluen))
array

#Plot the RGB image (THIS doesn't work)
plt.imshow(rgb)

# Plot histogram of the data
show_hist(raster, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype="stepfilled", title="Histogram of Landsat")
