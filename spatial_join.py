# -*- coding: utf-8 -*-
"""

spatial_join.py

How conduct spatila join using Geopandas


Created on Tue Nov 13 14:45:04 2018

@author: cscuser
"""

import geopandas as gpd

#Filepath
pop_fp = "L4_data/Vaestotietoruudukko_2015.shp"
point_fp = "L4_data/addresses.shp"

#Read the data
pop = gpd.read_file(pop_fp)
points = gpd.read_file(point_fp)

#Check that crs matches
assert pop.crs == points.crs, "The CRS of the layer do not match!"

# Ensure that the data is in the same projection
points = points.to_crs(crs=pop.crs)

#Make spatial join, information is stored into first one
#If the point is within the population then keep it
join = gpd.sjoin(points, pop, how="inner", op="within")

#What are the datatypes wihtin the columns
join.dtypes

#You get information about the diffent columns
join.describe

#Visualize, Markersize is telling how many people living in actual values
join.plot(column = "ASUKKAITA", cmap="Reds", markersize=join["ASUKKAITA"])

#here the percentice SEE Geoplot
join.plot(column = "ASUKKAITA", cmap="Reds", markersize=join["ASUKKAITA"]/1648*100)
