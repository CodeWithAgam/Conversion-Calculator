# The below function claculates the Area of a shapes
# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

import math

def calculate_area(shape_selected):

    shape_selected = shape_selected.input("Which shape's Area you want to calculate: ").lower()

    # check for the conditions
    if shape_selected == "rectangle":
        length = float(input("Enter the Length of Rectangle: "))
        breadth = float(input("Enter the Breadth of Rectangle: "))
        unit = input("Enter the Measuring Unit: ")
        
        # calculate the area of rectangle
        rect_area = round(length * breadth, 2)
        
        print(f"\nThe Area of Rectangle is {rect_area}{unit} squared.")

    elif shape_selected == "square":
        side = float(input("Enter the length of Square's Side: "))
        unit = input("Enter the Measuring Unit: ")

        # calculate the area of square
        square_area = round(side * side, 2)
        print(f"\nThe Area of Square is {square_area}{unit} squared.")

    elif shape_selected == "trapezium":
        trap_side1 = float(input("Enter the length of 1st Parallel Side: "))
        trap_side2 = float(input("Enter the length of 2nd Parallel Side: "))
        trap_height = input("Please enter height ")
        unit = input("Enter the Measuring Unit: ")
        
        # calculate the area of trapezium
        trapezium_area = round(0.5 * (trap_side1 + trap_side2) * trap_height, 2)
        print(f"\nThe Area of Trapezium is {trapezium_area}{unit} squared.")

    elif shape_selected == "triangle":
        
        triangle_type = int(input("Type 1 for Heron's Formula or 2 for Right Angled/Normal Triangle: ")).lower()

        if triangle_type == 1:
            side1 = input("Enter the length of Side1: ")
            side2 = input("Enter the length of Side2: ")
            side3 = input("Enter the length of Side3: ")
            semi_perimeter = (side1 + side2 + side3) / 2
            unit = input("Enter the Measuring Unit: ")

            # calculate the area of triangle
            triangle_area = round(math.sqrt(semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter -side3)), 2)
            print(f"\nThe Area of Triangle is {triangle_area}{unit} squared.")

        elif triangle_type == 2:
            height_tri = float(input("Enter the Triangle's height: "))
            base_tri = float(input("Enter the Triangle's base length: "))
            unit = input("Enter the Measuring Unit: ")        
            
            # calculate the area of right angled triangle
            triangle_area = round(0.5 * base_tri * height_tri, 2)
            print(f"\nThe Area of Right Angled Triangle is {triangle_area}{unit} squared.")

        else:
            print("Error! Please select 1 or 2.")

    elif shape_selected == "circle":
        radius = float(input("Enter the Circle's radius: "))
        unit = input("Enter the Measuring Unit: ")
        
        # calculate area of circle
        circle_area = round(math.pi * radius * radius, 2)
        print(f"\nThe Area of Circle is {circle_area}{unit} squared.")
            
    elif shape_selected == "parallelogram":
        base_parallelogram = float(input("Enter the Parallelogram's base: "))
        height_parallelogram = float(input("Enter the Parallelogram's height: "))
        unit = input("Enter the Measuring Unit: ")
        
        # calculate area of parallelogram
        parallelogram_area = round(base_parallelogram * height_parallelogram, 2)
        print(f"\nThe area of Parallelogram is {parallelogram_area}{unit} squared.")
        
    else:
        # this message gets printed if a shape entered by the user dosen't matches to the above conditions/shapes
        print("\nSorry! This shape is not available")

def Main():
    print("Calculate Area")
    calculate_area()
Main()