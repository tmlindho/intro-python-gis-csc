# -*- coding: utf-8 -*-
"""

raster.tools.py

Useful functions related to raster processing

Created on Wed Nov 14 10:26:30 2018

@author: cscuser
"""

import numpy as np
import json

def normalize(array):
    """
    Normalizes numpy arrays into scale 0.0 -1.0
    """
    array_min, array_max = array.min(), array.max()
    return ((array - array_min)/(array_max - array_min))

def get_features(gdf):
    """
    Converts GeoDataFrame into a format how
    rasterio mask function wants to have the geometric
    features.
    """
    features = [json.loads(gdf.to_json())["features"][0]["geometry"]]
    
    
    :

def getFeatures(gdf):
    """Function to parse features from GeoDataFrame in such a manner that rasterio wants them"""
    import json
    return [json.loads(gdf.to_json())['features'][0]['geometry']]

