# -*- coding: utf-8 -*-
"""
zonal_stats.py

How to calculate zonal statistics using rasterio and rasterstats

Created on Wed Nov 14 13:53:28 2018

@author: cscuser
"""

import rasterio
from rasterio.plot import show
from rasterstats import zonal_stats
import osmnx as ox
import geopandas as gpd
import os
import matplotlib.pyplot as plt
%matplotlib inline

# File path
data_dir = "L5_data"
dem_fp = os.path.join(data_dir, "Helsinki_DEM2x2m_Mosaic.tif")

# Read the Digital Elevation Model for Helsinki
dem = rasterio.open(dem_fp)
dem


# Fetch the Polygons for zonal statistics from OSM
kallio_q = "Kallio, Helsinki, Finland"
pihlajamaki_q = "Pihlajamäki, Malmi, Helsinki, Finland"

# Retrive geometries from OSM
kallio = ox.gdf_from_place(kallio_q)
pihlajamaki = ox.gdf_from_place(pihlajamaki_q)

# Projection of DEM and OSM places need to be the same
assert kallio.crs == dem.crs, "CRS do not match between the layers"
assert pihlajamaki.crs == dem.crs, " CRS do not match between the layers"

# Reroject
kallio = kallio.to_crs(crs= "+proj=utm +zone=35 +ellps=GRS80 +units=m +no_defs ")
pihlajamaki = pihlajamaki.to_crs(crs="+proj=utm +zone=35 +ellps=GRS80 +units=m +no_defs ")

kallio
kallio.plot()


# Plot the Polygons on top of the DEM
ax = kallio.plot(facecolor='None', edgecolor='red', linewidth=2)
ax = pihlajamaki.plot(ax=ax, facecolor='None', edgecolor='blue', linewidth=2)

# Plot DEM
show((dem, 1), ax=ax)

# There are something missing in between

# Which one is higher
if zs_kallio[0]["max"] > zs_pihlajamaki[0]["max"]:
    print("Kallio is higher")
else:
    print("Pihlajamäki si higher")