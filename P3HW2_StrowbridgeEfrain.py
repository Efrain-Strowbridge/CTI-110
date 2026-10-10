# Efrain Strowbridge
# 10/10/26
# P3HW2
# This program calculates the gross pay for an employee based on user inputted hours worked, pay rate, and overtime hours. And then prints the information in a formatted table.

# Variable Inputs
Employee_Name = input("Enter employee name: ")
Hours_Worked = int(input("Enter hours worked: "))
Pay_Rate = float(input("Enter regular pay rate: "))

# Calculate whether overtime hours were worked
if Hours_Worked > 40:
    Overtime_Hours = Hours_Worked - 40
else:
    Overtime_Hours = 0
# Calculate Regular Pay
Regular_Pay = (Hours_Worked - Overtime_Hours) * Pay_Rate
# Calculate Overtime Pay
Overtime_Pay = Overtime_Hours * (Pay_Rate * 1.5)
# Calculate Gross Pay
Gross_Pay = Regular_Pay + Overtime_Pay

def main():
    # Main output for all information
    print("----------------------------------------")
    print(f"Employee Name: {Employee_Name}")
    print()
    print(f"{'Hours Worked':<15} {'Pay Rate':<15} {'Overtime Hours':<18} {'Regular Hour Pay':<20} {'Overtime Pay':<18} {'Gross Pay':<15}")
    print("-----------------------------------------------------------------------------------------------------")
    print(f"{Hours_Worked:<15.1f} {Pay_Rate:<15.1f} {Overtime_Hours:<18.1f} {Regular_Pay:<20.2f} {Overtime_Pay:<18.2f} {Gross_Pay:<15.2f}")

main()