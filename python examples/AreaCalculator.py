"""
This is a program to calculate the area of circle or triangle.
Author:C2
"""

print "Program is running!"
option = raw_input("Enter C for circle or T for triangle: ")
if option.lower() == "c":
  radius = float(raw_input("Enter the radius for the circle: "))
  area = 3.13159*radius**2
  shape = "Cicle"
elif option.lower() == "t":
  base = float(raw_input("Enter the base for the triangle: "))
  height = float(raw_input("Enter the height for the triangle: "))
  area = base*height/2
  shape = "Triangle"
else:
  print "Wrong input!invalid shape!"
print "The area of the %s is %f" %(shape,area)
print "Program is exiting"
  
