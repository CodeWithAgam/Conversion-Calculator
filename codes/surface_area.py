# The below function claculates the Surface Area of a shapes
# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

def calculate_tsa():
    print("Calculate Total Surface Area!")
    name = input("Which shape's Total Surface Area you want to calculate: ").lower()

    # check for the conditions
    if name == "cuboid" or name == "rectangle":
        length = float(input("Length of Cuboid: "))
        breadth = float(input("Breadth of Cuboid: "))
        height = float(input("Height of Cuboid: "))
        unit = input("Enter the Measuring Unit: ")

        cuboid_sa = 2 * ((length * breadth) + (breadth * height) + (height * length))
        print(f"The Surface Area of Cuboid is {cuboid_sa}{unit} squared.")

    elif name == "cube" or name == "square":
        side = float(input("length of side of Cube: "))
        unit = input("Enter the Measuring Unit: ")

        square_sa = 6 * (side * side)
        print(f"The Surface Area of Cube is {square_sa}{unit} squared.")

    elif name == "cyclinder" or name == "right circular cyclinder" or name == "circular cyclinder":
        radiusCyclinder = float(input("Cyclinder's radius: "))
        heightCyclinder = float(input("Cyclinder's height: "))
        unit = input("Enter the Measuring Unit: ")

        cyclinder_sa = 2 * 3.14 * radiusCyclinder * (heightCyclinder + radiusCyclinder)
        print(f"The Surface Area of Cyclinder is {cyclinder_sa}{unit} squared.")
        
    else:
        # this message gets printed if a shape entered by the user dosen't matches to the above conditions/shapes
        print("Calculator: Sorry! This shape is not available")

calculate_tsa()