# Efrain Strowbridge
# 9/8/2026
# P1LAB1
# This program will ask the user for their full name and then greet them with a welcome message to the class.
from py_compile import main

firstname = input("Enter your First name: ")
lastname = input("Enter your Last name: ")

def main():
    print(f"Hello, {firstname + ' ' + lastname} ! Welcome to CTI-110.")
main()