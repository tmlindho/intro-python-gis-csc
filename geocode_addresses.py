# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 10:19:45 2018

geocode_address.py

How to convert addresses to Points

@author: cscuser
"""


# Import necessary modules
import pandas as pd
import geopandas as gpd
from geopandas.tools import geocode

#adds background maps
import contextily as ctx

print(ctx.sources)

# this takes you "frame" into account THIS IS NOT COMPLETE
def add_basemap(ax, zoom, url):
    xmin, xmax, ymin, ymax =ax.axis()
    def add_basemap(ax, zoom, url='http://tile.stamen.com/terrain/tileZ/tileX/tileY.png', basemap=None, extent=None):

   """Adds basemap to figure"""    

   xmin, xmax, ymin, ymax = ax.axis()

   if basemap is None:

       basemap, extent = get_basemap(ax, zoom=zoom, url=url)

   ax.imshow(basemap, extent=extent, interpolation='bilinear')

   # restore original x/y limits

   ax.axis((xmin, xmax, ymin, ymax))

   return ax



def get_basemap(ax, zoom, url='http://tile.stamen.com/terrain/tileZ/tileX/tileY.png'):

   """Helper function to add a basemap for the plot"""

   xmin, xmax, ymin, ymax = ax.axis()

   basemap, extent = ctx.bounds2img(xmin, ymin, xmax, ymax, zoom=zoom, url=url)

   return basemap, extent
# Filepath

fp = "L3_data/addresses.txt"

# Read the data
data = pd.read_csv(fp, sep=';')
data.columns

# Geocode addresses from addr
geo = geocode(data["addr"], provider="nominatim", user_agent ="csc_user_tml")

# Merge geocoded locations back to original DataFrame
geo = geo.join(data)

# Reproject to Wen Mercator, background maps don't work without this
geo = geo.to_crs(epsg=3857)
# Plot the data with background map
geo.plot()

#Add basemap, zoom tells how detailed map we want
add_basemap(ax=ax, zoom=12)

