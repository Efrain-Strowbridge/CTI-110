# Efrain Strowbridge
# 1o/26/26
# P4HW2
# This program calculates the gross pay for an indefinite amount of employees based on user inputted hours worked, pay rate, and overtime hours. It prints out the info for each employee until the user inputs "Done" and finally prints one final output showing the totals of all employees.

def main():
    # Preparation variable Inputs
    Employee_Count = 0
    Total_Overtime_Pay = 0.0
    Total_Regular_Pay = 0.0
    Total_Gross_Pay = 0.0
    Employee_Name = input("Enter employee's name or 'Done' to terminate: ")
    
    # The main loop that endlessly continues until the employee's name is "Done"
    while (Employee_Name != "Done"):
        # Variable Inputs
        Hours_Worked = float(input(f"How many hours did {Employee_Name} work? "))
        Pay_Rate = float(input(f"What is {Employee_Name}'s pay rate? "))

        # Calculates whether overtime hours were worked
        if Hours_Worked > 40:
            Regular_Hours = 40
            Overtime_Hours = Hours_Worked - 40
        else:
            Regular_Hours = Hours_Worked
            Overtime_Hours = 0
        # Calculates Regular Pay
        Regular_Pay = Regular_Hours * Pay_Rate
        # Calculates Overtime Pay
        Overtime_Pay = Overtime_Hours * Pay_Rate * 1.5
        # Calculates Gross Pay
        Gross_Pay = Regular_Pay + Overtime_Pay

        # Employee info output
        print("----------------------------------------")
        print(f"Employee Name: {Employee_Name}")
        print()
        print(f"{'Hours Worked':<15} {'Pay Rate':<15} {'Overtime Hours':<18} {'Regular Hour Pay':<20} {'Overtime Pay':<18} {'Gross Pay':<15}")
        print("-----------------------------------------------------------------------------------------------------")
        print(f"{Hours_Worked:<15.1f} {Pay_Rate:<15.1f} {Overtime_Hours:<18.1f} {Regular_Pay:<20.2f} {Overtime_Pay:<18.2f} {Gross_Pay:<15.2f}")
        
        # Adds data to the total for every loop
        Employee_Count += 1
        Total_Overtime_Pay += Overtime_Pay
        Total_Regular_Pay += Regular_Pay
        Total_Gross_Pay += Gross_Pay
        Employee_Name = input("Enter employee's name or 'Done' to terminate: ")
    
    # The ending output whenever the loop is broken
    print()
    print(f"Total number of employees entered: {Employee_Count}")
    print(f"Total amount paid for overtime: ${Total_Overtime_Pay:.2f}")
    print(f"Total amount paid for regular hours: ${Total_Regular_Pay:.2f}")
    print(f"Total amount paid in gross: ${Total_Gross_Pay:.2f}")

main()