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

    # Print the output
    print(f"Your Body Mass Index is {BMI}kg/m2")

if __name__ == "__main__" :
    print("the BMI or Body Mass Index")
    calculate_BMI()