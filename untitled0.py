# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 09:38:59 2018

@author: cscuser
"""

import rasterio
import os
import numpy as np
%matplotlib inline

# Data dir
data_dir = r"C:\IntroGIS\L5_data"
fp = os.path.join(data_dir, "Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif")

# Open the file:
raster = rasterio.open(fp)

# Check type of the variable 'raster'
type(raster)