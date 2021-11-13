# The below function claculates the Volume of a shapes
# Created by Agamdeep Singh / CodeWithAgam
# Insta: agamdeep_21
# Youtube: CodeWithAgam
# Github: CodeWithAgam

from math import *

print("Calculate Simple Interest")

# Ask for the inputs
Principal = float(input("Principal Amount: "))
RateOfInterest = float(input("Rate of Interest in Number: "))
TimePeriod = float(input("Time Period in Number: "))

# Calculate the Simple Interest and print it
simpleInterest = (Principal * RateOfInterest * TimePeriod) / 100
print(f"The Simple Interest is {simpleInterest}")