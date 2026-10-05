# Efrain Strowbridge
# 10/5/26
# P3LAB
# This program allows the user to enter a money value and calculates the most efficient number of dollars, quarters, dimes, nickels, and pennies needed to make the given amount of money.

#Variables and Math
money_value = float(input("Enter a money amount: "))
pennies = money_value * 100
dollars = int(pennies // 100)
remaining = int(pennies - dollars * 100)
quarters = int(remaining // 25)
remaining = int(remaining - quarters * 25)
dimes = int(remaining // 10)
remaining = int(remaining - dimes * 10)
nickels = int(remaining // 5)
remaining = int(remaining - nickels * 5)
pennies = int(remaining)

#The main function that prints the results of the calculations and singular/plural forms of the coin names.
def main():
    if money_value >= 0:
        if money_value == 0.00:
            print("No change can be made.")
        else:
            print("The most efficient change to break this down into is:")
            if dollars > 0:
                if dollars == 1:
                    print(f"{int(dollars)} Dollar")
                else:
                    print(f"{int(dollars)} Dollars")
            if quarters > 0:
                if quarters == 1:
                    print(f"{int(quarters)} Quarter")
                else:
                    print(f"{int(quarters)} Quarters")
            if dimes > 0:
                if dimes == 1:
                    print(f"{int(dimes)} Dime")
                else:
                    print(f"{int(dimes)} Dimes")
            if nickels > 0:
                if nickels == 1:
                    print(f"{int(nickels)} Nickel")
                else:
                    print(f"{int(nickels)} Nickels")
            if pennies > 0:
                if pennies == 1:
                    print(f"{int(pennies)} Penny")
                else:
                    print(f"{int(pennies)} Pennies")
    elif money_value < 0:
        print("Invalid input. Please get out of debt and try again later :]")

main()