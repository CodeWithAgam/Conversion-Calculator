# The below function claculates the Curved Surface Area of a Right Circular Cyclinder
# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

import math

def curved_sa():
    print("Calculate Curved Surface Area of Right Circular Cyclinder")

    # Ask for the inputs
    radius = float(input("Cyclinder's radius: "))
    height = float(input("Cyclinder's height: "))
    unit = input("Enter the Measuring Unit: ")

    # Calculate the Curved Surface Area and print it
    cyclinder_csa = 2 * math.pi * radius * height
    print(f"The Curved SA of your Cyclinder is {cyclinder_csa}{unit} squared.")

curved_sa()