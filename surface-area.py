# The below function claculates the Surface Area of a shapes
# Created by Agamdeep Singh / CodeWithAgam
# Insta: @coderagam001 / @agamdeep_21
# Youtube: CodeWithAgam
# Github: CodeWithAgam

from math import *

def calculate_sa(name):
    name = name.lower()

    # check for the conditions
    if name == "cuboid" or name == "rectangle":
        lenght = float(input("Length of Cuboid: "))
        breadth = float(input("Breadth of Cuboid: "))
        height = float(input("Height of Cuboid: "))
        
        # calculate Surface Area of rectangle
        cuboid_sa = 2 * ((lenght * breadth) + (breadth * height) + (height * lenght))
        print(f"The Surface Area of rectangle is {cuboid_sa}")

    elif name == "cube" or name == "square":
        side = float(input("Lenght of side of Cube: "))
        
        # calculate Surface Area of square
        square_sa = 6 * (side * side)
        print(f"The Surface Area of square is {square_sa}")


    elif name == "cyclinder" or name == "right circular cyclinder" or name == "circular cyclinder":
        radiusCyclinder = float(input("Cyclinder's radius: "))
        heightCyclinder = float(input("Cyclinder's height: "))

        # calculate Surface Area of circle
        cyclinder_sa = 2 * 3.14 * radiusCyclinder * (heightCyclinder + radiusCyclinder)
        print(f"The Surface Area of circle is {cyclinder_sa}")
        
    else:
        # this message gets printed if a shape entered by the user dosen't matches to the above conditions/shapes
        print("Calculator: Sorry! This shape is not available")

if __name__ == "__main__" :
    print("Calculate Surface Area")
    print("Calculator: Which shape's Surface Area you want to calculate?")
    shape_name = input("User: ")
    calculate_sa(shape_name)