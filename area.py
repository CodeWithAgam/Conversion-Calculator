# The below function claculates the Area of a shapes
# Created by Agamdeep Singh / CodeWithAgam
# Insta: @coderagam001 / @agamdeep_21
# Youtube: CodeWithAgam
# Github: CodeWithAgam

from math import *

def calculate_area(name):
    name = name.lower()

    # check for the conditions
    if name == "rectangle":
        lenght = float(input("Length of Rectangle: "))
        breadth = float(input("Breadth of Rectangle: "))
        
        # calculate area of rectangle
        rect_area = lenght * breadth
        print(f"The area of Rectangle is {rect_area}")

    elif name == "square":
        side = float(input("Lenght of side of square: "))
        
        # calculate area of square
        square_area = side * side
        print(f"The area of Square is {square_area}")

    elif name == "triangle":
        heightTri = float(input("Triangle's height: "))
        baseTri = float(input("Triangle's base length: "))
        
        # calculate area of triangle
        triangle_area = 0.5 * baseTri * heightTri
        print(f"The area of Triangle is {triangle_area}")

    elif name == "circle":
        radius = float(input("Circle's radius: "))

        # calculate area of circle
        circle_area = 3.14 * radius * radius
        print(f"The area of Circle is {circle_area}")
            
    elif name == "parallelogram":
        baseParallelogram = float(input("Parallelogram's base: "))
        heightParallelogram = float(input("Parallelogram's height: "))

        # calculate area of parallelogram
        parallelogram_area = baseParallelogram * heightParallelogram
        print(f"The area of Parallelogram is {parallelogram_area}")
        
    else:
        # this message gets printed if a shape entered by the user dosen't matches to the above conditions/shapes
        print("Calculator: Sorry! This shape is not available")

if __name__ == "__main__" :
    print("Calculate Area")
    print("Calculator: Which shape's area you want to calculate?")
    shape_name = input("User: ")
    calculate_area(shape_name)