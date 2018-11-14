# -*- coding: utf-8 -*-
"""

nearest_neighbour.py

How to get the nearest point of another one

Created on Tue Nov 13 15:11:14 2018

@author: cscuser
"""

from shapely.geometry import Point, MultiPoint
from shapely.ops import nearest_points
import geopandas as gpd

#Inside """ blaa blaa blaa """ you can write and is linked here to nearest and you can see with ctrl+I
# Again this doesn't work


def nearest(row, geom_union, df2, geom1_col='geometry', geom2_col='geometry', src_column=None):
   
    """
    
    Finds the closest point from a set of points
    
    Parameters
    ----------
    
    geom_union : shapely.MultiPoint
    """
    
    #Find the geometry that is closest, last number tells you like 1 is the closest, 2 second close etc.
    nearest =df2["geometry"] == nearest_points(row["geometry"], geom_union)[1]
    
    # Get the corresponding values from df2
    value = df2[nearest][src_column].get_values()[0]
    return value

# Filepaths
    fp1 = "L4_data/PKS_suuralue.kml"
    fp2 = "L4_data/addresses.shp"
    
    gpd.io.file.fiona.drvsupport.supported_drivers["KML"] = "rw"
    
    # Read data
    
    polys = gpd.read_file(fp1)
    src_points = gpd.read_file(fp2)
### FROM here on nonsense and the beginning doesn't work either

Unary_union = src_points.unary_union

polys["centroid"] = polys.centroid
     
    polys["nearest_id"] = polys.apply (neares, geom_union=unary_union, df1=polys, df2=src_points, geom1_col="centroid", axis=1)