# The below function claculates the Curved Surface Area of a Right Circular Cyclinder
# Created by Agamdeep Singh / CodeWithAgam
# Insta: @coderagam001 / @agamdeep_21
# Youtube: CodeWithAgam
# Github: CodeWithAgam

from math import *

print("Calculate Curved Surface Area of Right Circular Cyclinder")

# Ask for the inputs
radius = float(input("Cyclinder's radius: "))
height = float(input("Cyclinder's height: "))

# Calculate the Curved Surface Area and print it
cyclinder_csa = 2 * 3.14 * radius * height
print(f"The Curved SA of your Cyclinder is {cyclinder_csa}")