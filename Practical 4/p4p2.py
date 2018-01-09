
import math




lenght = float(input("Please enter the lenght of your square:"))
circumference = float(input("Please enter the circumference  of your circle:"))

square_area = lenght ** 2

widht = 172057.02
height = 172057.02
cube_volume1 = lenght **3

radius = circumference / 2
pi = 3.14
circle_area = radius ** 2 * pi

vsphere = 4 / 3
vradius = radius ** 3
volume_sphere = vsphere * pi * vradius

cyclinder_volume = pi * radius ** 2 * height

print ("This is the area of your square: ", square_area)
print ("This is the volume of your cube:", cube_volume1)
print ("This is the area of a circle: ", circle_area)
print ("This is the volume of a sphere: ", volume_sphere)
print("This is the volume of a cyclinder: ", cyclinder_volume)





