# The below function claculates the Perimeter of a shapes
# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

import math

def calculate_perimeter():

    shape_selected = input("Which shape's Perimeter you want to calculate: ").lower()
    
    if shape_selected == "rectangle":
        length = float(input("Enter the Length of Rectangle: "))
        breadth = float(input("Enter the Breadth of Rectangle: "))
        unit = input("Enter the Measuring Unit: ")

        # Calculate the Perimeter of the Rectangle 
        rect_perimeter = round(2 * (length + breadth), 2)
        print(f"\nThe Perimeter of Rectangle is {rect_perimeter}{unit}.")
    
    elif shape_selected == "square":
        side = float(input("Enter the Side of Square: "))
        unit = input("Enter the Measuring Unit: ")

        # Calculate the Perimeter of the Square
        square_perimeter = round(4 * side, 2)
        print(f"\nThe Perimeter of Square is {square_perimeter}{unit}.")
    
    elif shape_selected == "triangle":
        tri_side1 = float(input("Enter the length of Triangle's First side: "))
        tri_side2 = float(input("Enter the length of Triangle's Second side: "))
        tri_side3 = float(input("Enter the length of Triangle's Third side: "))
        unit = input("Enter the Measuring Unit: ")

        # Calculate the Perimeter of the Triangle
        triangle_perimeter = round(tri_side1 + tri_side2 + tri_side3, 2)
        print(f"\nThe Perimeter of Triangle is {triangle_perimeter}{unit}.")
    
    elif shape_selected == "circle":
        radius = float(input("Enter the Circle's radius: "))
        unit = input("Enter the Measuring Unit: ")

        # Calculate the Perimeter of the Circle
        circle_perimeter = round(2 * math.pi * radius, 2)
        print(f"\nThe Circumference of Circle is {circle_perimeter}{unit}.")            
    
    elif shape_selected == "parallelogram":
        para_side1 = float(input("Enter the length of Parallelogram's First side: "))
        para_side2 = float(input("Enter the length of Parallelogram's Second side: "))
        unit = input("Enter the Measuring Unit: ")

        # Calculate the Perimeter of the Parallelogram
        parallelogram_perimeter = round(2 * (para_side1 + para_side2), 2) 
        print(f"\nThe Perimeter of Parallelogram is {parallelogram_perimeter}{unit}.")        
    
    else:
        print("\nCalculator: Sorry! This shape is not available.")

def Main():
    print("Calculate Area")
    calculate_perimeter()
Main()