# Efrain Strowbridge
# 10/24/26
# P4LAB2
# This program gets the users input and calculates multiples up to twelve. Then, prints the equations and solutions. Finally, asks the user if they want to rerun the program again.

def main():
    # Defining boolean constant for the whole program.
    ContinueProgram = True
    # The main loop that calculates and prints multiplication equations.
    while (ContinueProgram):
        RerunLoop = True
        INT = int(input("Enter an integer: "))
        # An if statement to check for positive integers
        if (INT >= 0):
            result = INT * 1
            print(f"{INT} * 1 = {result}")
            result = INT * 2
            print(f"{INT} * 2 = {result}")
            result = INT * 3
            print(f"{INT} * 3 = {result}")
            result = INT * 4
            print(f"{INT} * 4 = {result}")
            result = INT * 5
            print(f"{INT} * 5 = {result}")
            result = INT * 6
            print(f"{INT} * 6 = {result}")
            result = INT * 7
            print(f"{INT} * 7 = {result}")
            result = INT * 8
            print(f"{INT} * 8 = {result}")
            result = INT * 9
            print(f"{INT} * 9 = {result}")
            result = INT * 10
            print(f"{INT} * 10 = {result}")
            result = INT * 11
            print(f"{INT} * 11 = {result}")
            result = INT * 12
            print(f"{INT} * 12 = {result}")
        else:
            print("Negative values are not accepted.")
        # A loop that either stops the main program or reruns it.
        while (RerunLoop):
            run_again = input("Do you want to run the program again? (y/n): ")
            if run_again == ("n"):
                ContinueProgram = False
                RerunLoop = False
            elif run_again == ("y"):
                ContinueProgram = True
                RerunLoop = False
            else:
                print("Invalid response.")
                RerunLoop = True
    # Ends the Program after the user decides so.
    print("'Program ended'")

main()