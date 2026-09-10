 # Efrain Strowbridge
 # 9/10/26
 # P1HW2
 # This Program calculates and displays travel expenses


# These constants calculate the travel expenses according to the user's input.
print("This Program calculates and displays travel epenses!")
Budget = int(input("Enter your Budget: "))
Destination = input("Enter your Destination: ")
Gas = int(input("How much do you plan to spend on gas: "))
Living = int(input("How much do you plan to spend on hotel/housing: "))
Food = int(input("How much do you need for food: "))
Remaining_Budget = Budget-(Gas+Living+Food)

def main():
    # This function executes the program by using the user's input to display the travel expenses.
    print()
    print("------Travel Expenses------")
    print(f"Location: {Destination}")
    print(f"Initial Budget: {Budget}")
    print()
    print(f"Gas Budget: {Gas}")
    print(f"Housing/Accomodation Budget: {Living}")
    print(f"Food Budget: {Food}")
    print()
    print(f"Remaining Balance: {Remaining_Budget}")

main()