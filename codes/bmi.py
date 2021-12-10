# The below function calculates the BMI or Body Mass Index of a person
# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

def calculate_BMI():
    # Get the inputs from the user
    height = float(input("Enter your height in M: "))
    weight = float(input("Enter your weight in KG: "))

    # Calculate the BMI or Body Mass Index
    # The formula is, weight(kg) / height^2(m^2)
    BMI = int(weight / height**2)

    # Check for the conditions and tell which category their BMI is.
    if BMI < 18.5:
        print(f"Your BMI is {BMI}, you are underweight!")

    elif BMI < 25:
        print(f"Your BMI is {BMI}, you have a normal weight!")

    elif BMI < 30:
        print(f"Your BMI is {BMI}, you are slightly overweight!")

    elif BMI < 35:
        print(f"Your BMI is {BMI}, you are obese!")
        
    else:
        print(f"Your BMI is {BMI}, you are clinically obese!")

print("Calculate the BMI or Body Mass Index")
calculate_BMI()