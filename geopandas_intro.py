# -*- coding: utf-8 -*-
"""

geopandas_intro.py

Basic functionalities of Geopandas library

Requirements
    - Geopandas

Created on Mon Nov 12 13:14:24 2018

@author: cscuser
"""

# Tools -> Preferences -> Ipython console -> graphics -> Graphics backend -> Automatic
# This will change your preferences so pictures are coming into separate window


# Import Geopandas 
# as command changes the name into a shorter version
import geopandas as gpd
import pandas as pd

# Filepath
fp = "L2_data/DAMSELFISH_distributions.shp"

# Read the file with Geopandas

data = gpd.read_file(fp)
type(data)

# Print the first rows of the data
data.head(data)
data.head()
data.head(10)
data.tail(19)

#Print column names of the GeoDataFrame
cols = data.columns
cols

# Plot the geometries
data.plot()

#Write the first 50 rows of our data into a new shapefile
outfp = "L2_data/DAMSELFISH_selection.shp"
output3 = "L2_data/DAMSELFISH_selection.geojson"
selection.to_file(output3, driver = "GeoJSON")

# Select the first rows
selection = data.head(50)

#Save selection to file
selection.to_file(outfp)

# some supported file forms
import fiona
fiona.supported_drivers

#Tanjan csv testi joka epaonnistui
outfp2 = "L2_data/DAMSELFISH_selection.csv"
selection = data.head(50)
selection.to_file(outfp2, driver = "csv")

#Geometries in GeoDataFrame

data.columns
data["geometry"].head()

sel3 = data[["geometry", "BINOMIAL"]].head()

# Select rows based on criteria

#Unique species can be found from the data
unique = data["BINOMIAL"].unique()
criteria = "Stegastes redemptus"

#Select rows based on criteria
#Look at these from automatingGSIProcesses and Pandas something
#log indexer you can take timeseries and something
fish_a = data.loc[data["BINOMIAL"]==criteria]
fish_a = data.loc[(data["ValueX"] > 10) & (data["ValueY"] < 100)]


import psycopg2
import geoalchemy2

#Initialize the connection with driver such as psycopg
conn, cursor = psycopg2.connect()
pgdata = gpd.read_postgis(sgl ="SELECT * FROM TABLEX FETCH FIRST 10 ROWS;", con=conn)

# Alternative 1: Iterate over GeoDataFrame JOKU ON TASSA VAARIN
for index,row in selection.iterrows():
        #Calculate the area of each Polygon
        poly_area = row["geometry"].area
        print(poly_area)

#Alternative2
        data["area"] = data.apply(lambda row: row["geometry"].area, axis=1)      
#Alternative3
def calculate_area(row):
    return row["geometry"].area
  
           data["area2"] = data.apply(calculate_area, axis=1)
# Geometric attributes from GeoDataFrame
    type(data)
#Calculate the area using geopandas directly, inside the brackets you define the column
data["area3"] = data.area   
data["centroid"] = data.centroid
data["centroid"].head()
data["geometry"].head()

#you can have different kind of geometries inside GeoDataFrame, but you can save only one format

#Set the geometry source for GeoDataFrame
geo = data.copy()
geo = geo.set_geometry("centroid")
geo.plot()

# Drop the "geometry" column from gdf
geo = geo.drop("geometry", axis=1)
geo.plot()

#Create a buffer from points
geo["buffer"]=geo.buffer(10)
# you need to activate what you see in a plot
geo = geo.set_geometry("buffer")
geo.plot()
#Save points
geo.to_file("gem_centroids.shp")

# Calculate basic statistics
mean_area = geo["area"].mean
min_area = geo["area"].min
max_area = geo["area"].max
std_area = geo["area"].std
madian_area = geo["area"].median

#Calculate in (Geo)DataFrame
geo["areasX2"] = geo["area1"] + geo ["area2"]
