# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 09:32:07 2018

read_wfs.py

@author: cscuser
"""

import geopandas as gpd
import requests
import geojson
import pycrs

#URl

url = "http://geo.stat.fi/geoserver/vaestoruutu/wfs"

#Get capabilities
capabilities_params = dict(service="WFS", request= "GetCapabilites")


# Request
capabilities = requests.get(url, params=capabilities_params)
print(capabilities.content)


#specify the parameter for feching the data

params = dict(service="WFS", version="2.0.0", request ="GetFeature", typeName="vaestoruutu:vaki2017_5km", outputFormat ="json")

#Fetch the data from WFS

r = requests.get(url, params=params)

type(r)

# Create a GeoDataFrame from the response
data = gpd.GeoDataFrame.from_features(geojson.loads(r.content))

#Define CRS

data.crs = {"init": "epsg:3067"}

#Define CRS using pycrs

data.crs = pycrs.parser.from_epsg_code(3067).to_proj4()
data.crs

#Set geometry
data = data.set_geometry("geometry")

#Remove colums with lists
data =data.drop("bbox", axis=1)
# Save to disk

outfp = "L2_data/Population_grid_5km.shp"
data.to_file(outfp)
