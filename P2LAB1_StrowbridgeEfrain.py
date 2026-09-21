# Efrain Strowbrisge
# 9/21/26
# P2LAB1

# Program will calculate and display the diameter, circumference, and area of a circle with a user input radius.
# 1. The program takes radius from user.
# 2. Calculates the diameter, circumference, and area of a circle using the radius.
# 3. Displays the results to the user.

def main():
    diameter = radius * 2
    circumference = 2 * pi * radius
    area = pi * radius ** 2
    print()
    print(f"The diameter of the circle is {diameter:.1f}")
    print()
    print(f"The circumference of the circle is {circumference:.2f}")
    print()
    print(f"The area of the circle is {area:.3f}")

pi = 3.14159265359
radius = float(input("What is the radius of the circle? "))
main()