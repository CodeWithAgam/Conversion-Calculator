# The below function claculates the Area of 4 walls of Cube and Cuboid
# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

def calculate_4wa(name):
    name = name.lower()

    # check for the conditions
    if name == "cuboid" or name == "rectangle":
        lenght = float(input("Length of Cuboid: "))
        breadth = float(input("Breadth of Cuboid: "))
        height = float(input("Height of Cuboid: "))
        
        # calculate  Area of rectangle
        cuboid_4wa = 2 * ((lenght * breadth) + (breadth * height) + (height * lenght))
        print(f"The  Area of rectangle is {cuboid_4wa}")

    elif name == "cube" or name == "square":
        side = float(input("Lenght of side of Cube: "))
        
        # calculate  Area of square
        square_4wa = 6 * (side * side)
        print(f"The  Area of square is {square_4wa}")

        
    else:
        # this mes4wage gets printed if a shape entered by the user dosen't matches to the above conditions/shapes
        print("Calculator: Sorry! This shape is not available")

if __name__ == "__main__" :
    print("Calculate Area of 4 Walls of Cube and Cuboid")
    print("Calculator: Which shape's 4 Wall's Area you want to calculate?")
    shape_name = input("User: ")
    calculate_4wa(shape_name)