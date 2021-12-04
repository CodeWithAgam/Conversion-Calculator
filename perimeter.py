# The below function claculates the Perimeter of a shapes
# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

def calculate_perimeter(name):
    name = name.lower()
    
    if name == "rectangle":
        lenght = float(input("Length of Rectangle: "))
        breadth = float(input("Breadth of Rectangle: "))        
        rect_perimeter = 2 * (lenght + breadth)
        print(f"The Perimeter of Rectangle is {rect_perimeter}")
    
    elif name == "square":
        side = float(input("Side of Square: "))
        square_perimeter = 4 * side
        print(f"The Perimeter of Square is {square_perimeter}")
    
    elif name == "triangle":
        TriSide1 = float(input("First side of triangle: "))
        TriSide2 = float(input("Second side of triangle: "))
        TriSide3 = float(input("Third side of triangle: "))
        triangle_perimeter = TriSide1 + TriSide2 + TriSide3
        print(f"The Perimeter of Triangle is {triangle_perimeter}")
    
    elif name == "circle":
        radius = float(input("Circle's radius: "))
        circle_perimeter = 2 * 3.14 * radius
        print(f"The Circumference of Circle is {circle_perimeter}")            
    
    elif name == "parallelogram":
        ParallelogramSide1 = float(input("Parallelogram's first side: "))
        ParallelogramSide2 = float(input("Parallelogram's second side: "))
        parallelogram_perimeter = 2 * (ParallelogramSide1 + ParallelogramSide2) 
        print(f"The Perimeter of Parallelogram is {parallelogram_perimeter}")        
    
    else:
        print("Calculator: Sorry! This shape is not available")

if __name__ == "__main__" :
    print("Calculate Perimeter")
    print("Calculator: Which shape's perimeter you want to calculate?")
    shape_name = input("User: ")
    calculate_perimeter(shape_name)