# The below program claculates Compound Interest
# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

def CI():
    print("Calculate Compound Interest!")

    principal = float(input("Principal Amount: "))
    rate = float(input("Rate of Interest: "))
    time = float(input("Time Period in Years: "))
    payable = int(input("\nType 1 if the interest is payable Yearly, 2 if Hear-Yearly or 3 if Quarterly: "))

    if payable == 1:
        amount = principal * (1 + rate / 100) ** time
        compound_interest = amount - principal
        print(f"\nThe Compound Interest is {compound_interest} and Amount is {amount}")
    
    elif payable == 2:
        amount = principal * (1 + rate / 100) ** (2 * time)
        compound_interest = amount - principal
        print(f"\nThe Compound Interest is {compound_interest} and Amount is {amount}")

    elif payable == 3:
        amount = principal * (1 + rate / 100) ** (4 * time)
        compound_interest = amount - principal
        print(f"\nThe Compound Interest is {compound_interest} and Amount is {amount}")
    
    else:
        print("\nError! Please type 1, 2 or 3.")

CI()