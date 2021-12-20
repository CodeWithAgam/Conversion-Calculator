# The below program claculates the Area of 4 walls of Cube and Cuboid.
# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

def calculate_4wa():
    print("Calculate Area of 4 Walls of Cube or Cuboid!")
    name = input("Which shape you want to calculate: ").lower()

    # check for the conditions
    if name == "cuboid" or name == "rectangle":
        length = float(input("Enter the length of Cuboid: "))
        breadth = float(input("Enter the breadth of Cuboid: "))
        height = float(input("Enter the height of Cuboid: "))
        unit = input("Enter the Measuring Unit: ")
        
        cuboid_4wa = 2 * height * (length + breadth)
        print(f"The Area of 4 Walls of Cuboid is {cuboid_4wa}{unit} squared.")

    elif name == "cube" or name == "square":
        side = float(input("Enter the length of side of Cube: "))
        unit = input("Enter the Measuring Unit: ")
        
        square_4wa = 6 * (side ** 2)
        print(f"The Area of 4 wwalls of Cube is {square_4wa}{unit} squared.")

    else:
        print("Calculator: Sorry! This shape is not available")

calculate_4wa()