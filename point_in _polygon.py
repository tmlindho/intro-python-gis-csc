# -*- coding: utf-8 -*-
"""

point_in _polygon.py

Ho to conduct Point iin Polygon queries with geoPandas

Created on Tue Nov 13 13:46:51 20

@author: cscuser
"""

import geopandas as gpd
import matplotlib.pyplot as plt
import shapely.speedups 
gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'
shapely.speedups.enable()



#Filepath

fp = "L4_data/PKS_Suuralue.kml"
fpa = "L4_data/addresses.shp"


#Read file
polys = gpd.read_file(fp, driver = "KML")
data = gpd.read_file(fpa)

#Select area of intersect
southern = polys.loc[polys["Name"]== "Eteläinen"]

#Reset index and drop the original index column
southern =southern.reset_index(drop=True)

#Conduct Point in Polygon query (data must be in same coordinate system)
# You need to extract the polygon from the GeoDataFrame
pip_mask = data.within(southern.loc[0, "geometry"])
type(pip_mask)

#Select the points that were within the Polygon
pip_data = data.loc[pip_mask]

#Visualize the selection
ax = polys.plot(facecolor = "gray")
ax = southern.plot(ax=ax, facecolor="yellow")
ax = pip_data.plot(ax=ax, color="red", markersize=3)
