# Efrain Strowbridge
# 10/7/26
# P3HW1
# This program takes a number grade, determines average and displays letter grade for the average.

# Enter grades for six modules.
Mod1 = float(input("Enter grade for Module 1: "))
Mod2 = float(input("Enter grade for Module 2: "))
Mod3 = float(input("Enter grade for Module 3: "))
Mod4 = float(input("Enter grade for Module 4: "))
Mod5 = float(input("Enter grade for Module 5: "))
Mod6 = float(input("Enter grade for Module 6: "))

# Add grades to a list, and calculate the lowest, highest, sum, and average.
Grades = [Mod1, Mod2, Mod3, Mod4, Mod5, Mod6]
Lowest = min(Grades)
Highest = max(Grades)
Sum = sum(Grades)
Average = Sum / len(Grades)

def main():
    # Print the lowest, highest, sum, average, and the letter grade for average
    print()
    print("------------Results------------")
    print(f'Lowest Grade: {Lowest:15.1f}')
    print(f'Highest Grade: {Highest:15.1f}')
    print(f'Sum of Grades: {Sum:15.1f}')
    print(f'Average Grade: {Average:15.2f}')
    print("-------------------------------")
    if Average >= 90:
        print("Your grade is an A!! :D")
    elif Average >= 80:
        print("Your grade is a B! :)")
    elif Average >= 70:
        print("Your grade is a C :|")
    elif Average >= 60:
        print("Your grade is a D. :(")
    else:
        print("Your grade is an F.. >:(")

main()