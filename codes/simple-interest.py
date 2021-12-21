# The below program claculates Simple Interest
# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

def SI():
    print("Calculate Simple Interest")

    principal = float(input("Principal Amount: "))
    rate = float(input("Rate of Interest in Number: "))
    time = float(input("Time Period in Number: "))
    currency = float(input("Enter the currency you want to use: "))

    simple_interest = (principal * rate * time) / 100
    print(f"The Simple Interest is {currency}{simple_interest}.")

SI()