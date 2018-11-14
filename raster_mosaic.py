# -*- coding: utf-8 -*-
"""
raster_mosaic.py

How to create raster mosaic using Rasterio

Created on Wed Nov 14 13:20:45 2018

@author: cscuser
"""

import rasterio
from rasterio.merge import merge
from rasterio.plot import show
import glob
import os
import pycrs
%matplotlib inline

# File and folder paths
data_dir = "L5_data"

# Output filepath for the mosaic
out_fp = os.path.join(data_dir, "Helsinki_DEM2x2m_Mosaic.tif")

# Make a search criteria to select the DEM files
search_criteria = "L*.tif"
q = os.path.join(data_dir, search_criteria)
print(q)

# List files that matches the criteria
dem_fps = glob.glob(q)
dem_fps

# Open the source files with rasterio
# len gives the amount of files, charactor etc
src_files_to_mosaic = [ rasterio.open(fp) for fp in dem_fps ]
len(src_files_to_mosaic)

#  Merge rasters into mosaic
mosaic, out_trans = merge(datasets=src_files_to_mosaic)

# Plot
show(mosaic, cmap="terrain")
#plt.imshow(mosaic, cmap="terrain")
#plt.colorbar()

# Save the mosaic and update the metadata
# Here the metadata is a copy of one file and needs to be update
out_meta = src_files_to_mosaic[0].meta.copy()

# Update metadata with new dimensions and crs
out_meta.update(
        {"height" : mosaic.shape[1],
         "width" :mosaic.shape[2],
         "transform": out_trans,
         "crs": "+proj=utm +zone=35 +ellps=GRS80 +units=m +no_defs "
         }
        )

# Write the mosaic to disk
with rasterio.open(out_fp, "w", **out_meta) as dest:
    dest.write(mosaic)
    
# Plot    
m = rasterio.open(out_fp)
plt.imshow(m.read(1), cmap="terrain")
plt.colorbar()    


