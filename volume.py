# The below function claculates the Volume of a shapes
# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

def calculate_volume(name):
    name = name.lower()

    # check for the conditions
    if name == "cuboid" or name == "rectangle":
        lenght = float(input("Length of Cuboid: "))
        breadth = float(input("Breadth of Cuboid: "))
        height = float(input("Height of Cuboid: "))
        
        # calculate volume of rectangle
        cuboid_volume = lenght * breadth * height
        print(f"The volume of rectangle is {cuboid_volume}")

    elif name == "cube" or name == "square":
        side = float(input("Lenght of side of Cube: "))
        
        # calculate volume of square
        square_volume = side * side * side
        print(f"The volume of square is {square_volume}")


    elif name == "circle" or name == "cyclinder" or name == "right circular cyclinder" or name == "circular cyclinder":
        radiusCyclinder = float(input("Cyclinder's radius: "))
        heightCyclinder = float(input("Cyclinder's height: "))

        # calculate volume of circle
        cyclinder_volume = 2 * 3.14 * radiusCyclinder * heightCyclinder
        print(f"The volume of circle is {cyclinder_volume}")
        
    else:
        # this message gets printed if a shape entered by the user dosen't matches to the above conditions/shapes
        print("Calculator: Sorry! This shape is not available")

if __name__ == "__main__" :
    print("Calculate Volume")
    print("Calculator: Which shape's volume you want to calculate?")
    shape_name = input("User: ")
    calculate_volume(shape_name)