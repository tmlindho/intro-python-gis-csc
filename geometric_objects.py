# -*- coding: utf-8 -*-
"""
geometric_objects.py

Working with shapely package creating geometric objects and looking at their functionalities.

Requirements
    - shapely
    
Notes:
    - First taste of Python GIS

Created on Mon Nov 12 10:58:55 2018

@author: cscuser
"""


# This imports the whole package "import shapely"
# Import necessary geometric objects from shapely module

from shapely.geometry import Point, LineString, Polygon


#Point
# -----


# Create Point geometric object(s) with coordinates
point1 = Point(2.2, 4.2)
point1
print(point1)
point2 = Point(7.2, -25.1)
point3 = Point(9.26, -2.456)
point3D = Point(9.26, -2.456, 0.57)

print(point3D)
type(point1)
# What is the type of the point?
point_type = type(point1)

#get coordinates
point_coords = point1.coords
point_coords

#get xy

xy = point1.xy
print(xy)

#get x and y coordinates
x = point1.x
y = point1.y 

# calculate distance between point1 and point 2
point_dis = point1.distance(point2)
print(point_dis)

# Create a buffer with distance of 20
point_buffer = point1.buffer(20)
point_buffer


#LineString
# --------

#Create line based on Shapely points
line = LineString([point1, point2, point3])
line

#Create line based on coordinate tuples
line2 = LineString([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])

#Coordinates
lxy = line.xy
print(lxy)

# Get x and y coordinates
x = line.xy[0]
y = line.xy[1]
list(y)


#Get the length
l_length = line.length

#Get the centroid of the line
l_centroid =line.centroid
l_centroid

#Polygon
# -----

#Create polygon based on coordinate tuples
poly = Polygon([(2.2, 4.2), (7.2, -25,1), (9.26, -2.456)])


#Create polygon based on points
point_list = [point1, point2, point3]
poly2 = Polygon([(p.x, p.y) for p in point_list])
poly2

# Get geometry type as string
poly_type = poly.geom_type

#Calculate the area
poly_area = poly.area

# Centroid
poly.centroid

#Bounding box
poly_bbox = poly.bounds

#Create Bounding Box geometry
#asterix unpacks the value
from shapely.geometry import box
#unpack the bounding box coordinates with asterix *
bbox =  box(*poly_bbox)

#Get exterior
poly_exterior = poly.exterior

#Lenght of the exterior
poly_ext_length = poly.exterior.length

# Polygon with hole(s)
#Exterior of the world in decimal degrees
world_exterior = [(-180, 90), (-180, -90), (180, -90), (180, 90)]

# Let's create a hole --> remember there can be multiple holes, thus we need to have a list of hole(s).
# Here we have just one.
west_hole = [[(-170, 80), (-170, -80), (170, -80), (170, 80)]]

world_poly = Polygon(shell=world_exterior, holes = west_hole)
