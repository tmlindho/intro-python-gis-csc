# -*- coding: utf-8 -*-
"""
data_classificaion.py

Classify values based on common classifiers

Created on Tue Nov 13 13:08:30 2018

@author: cscuser
"""

import geopandas as gpd
import pysal as ps

# Filepath
fp = "L3_data/TravelTimes_to_5975375_RailwayStation_Helsinki.geojson"

#Read the data
data =  gpd.read_file(fp)


# Exclude -1 (no data) values
data = data.loc[data["pt_r_tt"]>=0]

# Plot using 9 classes based on Fisher Jenks
data.plot(column = "pt_r_tt", scheme = "Fisher_Jenks", k=9, cmap="RdYlBu", linewidth = 0, legend=True)

# Define the number of classes
k = 12

# Initialize the natural breaks classifier
classifier = ps.Natural_Breaks.make(k)

#Classify the travel time values
classifications = data[["pt_r_tt"]].apply(classifier)


# Rename the column "nb_pt_r_tt" You can rename multiple columns at the same time. Just put those inside brackets and separate with comma
classifications = classifications.rename(columns = {"pt_r_tt": "nb_r_tt"})

# Conduct table join bsed on index
data = data.join(classifications)
                 
 #Create a map based on new classes
 data.plot(column ="nb_r_tt", linewidth = 0, legend=True)

#Create a custom classifier
 class_bins = [10, 20, 30, 40, 50, 60]
 classifier = ps.User_Defined.make(class_bins)
 
 #Classify the travel time values TAHAN TULEE JOKU VIRHE
custom_classifications = data[["pt_r_tt"]].apply(classifier)


# Rename the column "nb_pt_r_tt" You can rename multiple columns at the same time. Just put those inside brackets and separate with comma
custom_classifications = classifications.rename(columns = {"pt_r_tt": "c_pt_r_tt"})

# Conduct table join bsed on index
data = data.join(custom_classifications)

ax=data.plot(column ="c_pt_r_tt", linewidth = 0, legend=True)
