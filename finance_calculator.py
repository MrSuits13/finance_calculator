# Lets import the math 
import math 
# this program will allow the user to choose between two different financial calculators : investment and home loan repayment calculator 
# enter the first output that the user sees
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
# printing the space between below
print()
# assigning a variable called calculator_type and getting the input from the user of the type of calculator they want to use 
calculator_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
# using .lower() function in order for the user to use "Bond" , "BOND" or "bond"
if calculator_type.lower() == "bond":
    print("bond calculator selected.")
elif calculator_type.lower() == "investment":
    print("investment calculator selected.")
else:
    print("Invalid option selected!")
# if the user selects "investment" ask the user to input the following:
# the amount of money that the are depositing and assign to a variable money_invested
if calculator_type.lower() == "investment":
    money_invested = float(input("Enter the amount of money that you are depositing?: "))
    interest_rate = float(input("Enter the interest rate?: "))
    number_of_years = int(input("Enter the number of years you plan on investing the money?: "))
    interest = input("Choose the type of interest simple/compound?: ")
    if interest.lower() == "simple":
        money_receive = money_invested * (1 + (interest_rate/100) * number_of_years)
        print(f"The amount you will receive after {number_of_years} years is R {money_receive} ")
