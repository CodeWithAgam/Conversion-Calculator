# The below function calculates the Volume of a shapes
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
        length = float(input("Length of Cuboid: "))
        breadth = float(input("Breadth of Cuboid: "))
        height = float(input("Height of Cuboid: "))
        unit = input("Enter the Measuring Unit: ")
        
        # calculate volume of rectangle
        cuboid_volume = length * breadth * height
        print(f"The volume of rectangle is {cuboid_volume} {unit}cubed.")

    elif name == "cube" or name == "square":
        side = float(input("Length of side of Cube: "))
        
        # calculate volume of square
        square_volume = side * side * side
        print(f"The volume of square is {square_volume}")


    elif name == "circle" or name == "cylinder" or name == "right circular cylinder" or name == "circular cylinder":
        radius_cylinder = float(input("Cylinder's radius: "))
        height_cylinder = float(input("Cylinder's height: "))

        # calculate volume of circle
        cylinder_volume = 2 * 3.14 * radius_cylinder * height_cylinder
        print(f"The volume of circle is {cylinder_volume}")
        
    else:
        # this message gets printed if a shape entered by the user doesn't match the above conditions/shapes
        print("Calculator: Sorry! This shape is not available")

if __name__ == "__main__" :
    print("Calculate Volume")
    print("Calculator: Which shape's volume you want to calculate?")
    shape_name = input("User: ")
    calculate_volume(shape_name)