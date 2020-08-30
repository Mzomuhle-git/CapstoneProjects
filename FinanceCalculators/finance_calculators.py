# This program is financial calculator for calculating an investment and home loan repayment amount
# r - is the interest rate
# P - is the amount that the user deposits / current value of the house
# t - is the number of years that the money is being invested for.
# A - is the total amount once the interest has been applied.
# n - is the number of months over which the bond will be repaid.
# i - is the monthly interest rate, calculated by dividing the annual interest rate by 12.

# To include extended mathematical functions
import math

print("Choose either 'investment' or 'bond' from the menu below to proceed: ")
print("investment \t - to calculate the amount of interest you'll earn on interest ")
print("bond \t \t - to calculate the amount you'll have to pay on a home loan")
calculator_type = input(": ")

# choosing investment or bond
if calculator_type == "investment" or calculator_type == "Investment" or calculator_type == "INVESTMENT":
    P = float(input("Enter the amount of money to deposit: "))
    t = int(input("Enter the number of years: "))
    interest_rate = float(input("Enter the percentage interest rate: "))
    interest = input("Enter the type of interest [compound or simple] interest: ")
    r = interest_rate / 100

    if interest == "simple" or interest == "SIMPLE" or interest == "Simple":
        # Formula for calculating simple interest
        A = P * (1 + r * t)
        A = round(A, 2)
        print("The total amount of money the user will earn is: R", A)
    elif interest == "compound" or interest == "COMPOUND" or interest == "Compound":
        # Formula for calculating compound
        A = P * math.pow((1 + r), t)
        A = round(A, 2)
        print("The total amount of money the user will earn is: \t R", A)

    # prints the error massage
    else:
        print("Error!!! Please choose the correct word [simple or compound] and try again")

elif calculator_type == "bond" or calculator_type == "BOND" or calculator_type == "Bond":
    P = float(input("Enter the current value of the house: "))
    interest_rate = float(input("Enter the annual interest rate: "))
    n = int(input("Enter the number of months to repay: "))
    r = interest_rate / 100
    i = r / 12
    # Formula for calculating bond repayment amount
    repayment = (i * P) / (1 - (1 + i) ** (-n))
    repayment = round(repayment, 2)
    print("After each month the user will need to pay: \t R", repayment)

# prints the error massage if the user doesn't enter investment or bond
else:
    print("Error!!! Please enter the correct word [investment or bond] and try again")
