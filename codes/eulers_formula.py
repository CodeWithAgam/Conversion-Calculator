# The below program verifies Euler's Formula for solids
# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

def eulers_formula():
    print("Verify Euler's Formula for solids!")

    faces = int(input("\nEnter the number of Faces: "))
    edges = int(input("Enter the number of Edges: "))
    verticies = int(input("Enter the number of Verticies: "))

    output = (verticies + faces) - edges

    print(f"\nFaces + Verticies - Edges = 2. Your output is {output}.")

eulers_formula()