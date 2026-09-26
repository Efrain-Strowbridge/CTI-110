# Efrain Strowbridge
# 9/25/26
# P2HW1
# This Program calculates and displays travel expenses


# These constants calculate the travel expenses according to the user's input.
print("This Program calculates and displays travel epenses!")
Budget = float(input(f"Enter your Budget: "))
Destination = input("Enter your Destination: ")
Gas = float(input(f"How much do you plan to spend on gas: "))
Living = float(input(f"How much do you plan to spend on hotel/housing: "))
Food = float(input(f"How much do you need for food: "))
Remaining_Budget = Budget-(Gas+Living+Food)

def main():
    # This function executes the program by using the user's input to display the travel expenses.
    print("--------------Travel Expenses--------------")
    print(f'{"Location: ":30}{Destination}')
    print(f'{"Initial Budget: ":30}${Budget:.2f}')
    print(f'{"Gas Budget: ":30}${Gas:.2f}')
    print(f'{"Housing/Accomodation Budget: ":30}${Living:.2f}')
    print(f'{"Food Budget: ":30}${Food:.2f}')
    print("-------------------------------------------")
    print()
    print(f'{"Remaining Balance: ":30}${Remaining_Budget:.2f}')

main()
