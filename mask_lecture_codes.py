# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 12:53:44 2018

@author: cscuser
"""

import rasterio
from rasterio.plot import show
from rasterio.plot import show_hist
from rasterio.mask import mask
from shapely.geometry import box
import geopandas as gpd
from fiona.crs import from_epsg
import pycrs
import os
%matplotlib inline

# Data dir
data_dir = "L5_data"

# Input raster
fp = os.path.join(data_dir, "p188r018_7t20020529_z34__LV-FIN.tif")

# Output raster
out_tif = os.path.join(data_dir, "Helsinki_Masked.tif")

# Read the data
data = rasterio.open(fp)

# Visualize the NIR band
show((data, 4), cmap='terrain')


# WGS84 coordinates
minx, miny = 24.60, 60.00
maxx, maxy = 25.22, 60.35
bbox = box(minx, miny, maxx, maxy)

geo = gpd.GeoDataFrame({'geometry': bbox}, index=[0], crs=from_epsg(4326))
print(geo)
# Project the Polygon into same CRS as the grid
geo = geo.to_crs(crs=data.crs.data)

# Print crs
geo.crs
def getFeatures(gdf):
    """Function to parse features from GeoDataFrame in such a manner that rasterio wants them"""
    import json
    return [json.loads(gdf.to_json())['features'][0]['geometry']]

coords = getFeatures(geo)
print(coords)
out_img, out_transform = mask(dataset=data, shapes=coords, crop=True)
# Copy the metadata
out_meta = data.meta.copy()
print(out_meta)
epsg_code = int(data.crs.data['init'][5:])
print(epsg_code)
out_meta.update({"driver": "GTiff",
                 "height": out_img.shape[1],
                 "width": out_img.shape[2],
                 "transform": out_transform,
                 "crs": pycrs.parser.from_epsg_code(epsg_code).to_proj4()}
                         )

with rasterio.open(out_tif, "w", **out_meta) as dest:
        dest.write(out_img)


# Open the clipped raster file
clipped = rasterio.open(out_tif)

# Visualize
show((clipped, 5), cmap='terrain')

