#Filename q2_calc_cylinder_volume.py
#author:wzx
#Computing the volume of a cylinder

#main

#prompt and get radius
radius=int(input("Enter radius : "))
#calculate area
import math
area=radius**2*math.pi
#prompt and get length
length=int(input("Enter length : "))
#calculate volume
volume=area*length
#output
print("Volume = ",volume)
