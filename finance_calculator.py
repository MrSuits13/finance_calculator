# Lets import the math 
import math 

# Function to calculate Return on Investment (ROI)
def calculate_roi(initial_investment, final_value):
    """
    Calculate Return on Investment (ROI).
    Formula: ROI = ((final value - initial investment) / initial investment) * 100
    """
    roi = ((final_value - initial_investment) / initial_investment) * 100
    return roi

# Function to calculate bond repayment
def calculate_bond_repayment(present_value, interest_rate, number_of_months):
    """
    Calculate bond repayment.
    """
    monthly_interest_rate = (interest_rate / 100) / 12
    repayment = (monthly_interest_rate * present_value) / (1 - (1 + monthly_interest_rate) ** (-number_of_months))
    return round(repayment, 2)

# this program will allow the user to choose between two different financial calculators: investment and home loan repayment calculator 
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
    interest_type = input("Choose the type of interest simple/compound?: ")
    
    # creating the if statement for simple and compound
    if interest_type.lower() == "simple":
        money_receive = money_invested * (1 + (interest_rate/100) * number_of_years)
        print(f"The amount you will receive after {number_of_years} years is R {money_receive} ")
        
        # Calculate and display ROI
        roi = calculate_roi(money_invested, money_receive)
        print(f"The Return on Investment (ROI) after {number_of_years} years is {roi:.2f}%")
    elif interest_type.lower() == "compound":
        money_receive = money_invested * (math.pow(1 + (interest_rate / 100), number_of_years))
        # rounding to two decimals
        money_receive_rounded = round(money_receive, 2)
        print(f"The amount you will receive after {number_of_years} years is R {money_receive_rounded} ")
        
        # Calculate and display ROI
        roi = calculate_roi(money_invested, money_receive)
        print(f"The Return on Investment (ROI) after {number_of_years} years is {roi:.2f}%")
    else:
        print("Invalid Option!")

# lets do the bond repayment calculator 
# lets start by creating the variables and calculating the answer using the formula 
elif calculator_type.lower() == "bond":
    present_value = int(input("Enter the present value of the house?: "))
    interest_rate = float(input("Enter the interest rate?: "))
    number_of_months = int(input("Enter the number of months you plan to repay the bond?: "))
    
    repayment = calculate_bond_repayment(present_value, interest_rate, number_of_months)
    
    # printing the monthly repayment amount
    print(f"You will have a monthly repayment of R{repayment} per month")
