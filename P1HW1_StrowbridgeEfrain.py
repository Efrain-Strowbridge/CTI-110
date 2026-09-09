 # Efrain Strowbridge
 # 9/9/26
 # P1HW1
 # This program will calculate the exponential, addition and subtraction solutions to integers that the user inputs.

def main():
    print("---------Calculating Exponents---------")
    print()
    print()
    Base = int(input("Enter a base number: "))
    Exponent = int(input("Enter an exponent: "))
    Result = Base ** Exponent
    print()
    print()
    print(f"{Base}, raised to the power of {Exponent}, is {Result}!!")
    print()
    print()
    print("--------Addition and Subtraction--------")
    print()
    print()
    num1 = int(input("Enter a starting integer: "))
    num2 = int(input("Enter an integer to add: "))
    num3 = int(input("Enter an integer to subtract: "))
    sum_solution = num1 + num2
    final_solution = sum_solution - num3
    print()
    print()
    print(f"If, {num1} + {num2} is equal to {sum_solution}")
    print(f"And, {sum_solution} - {num3} is equal to {final_solution}")
    print(f"Then, {num1} + {num2} - {num3} is equal to {final_solution}")

main()