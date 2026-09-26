# Efrain Strowbridge
# 9/26/26
# P2HW2
# This program will ask the user to input 6 grades; then display the minimum, maximum, sum and average of the grades.

print("---------------------------------------")
M1 = float(input(f'{"Enter grade for Module 1: ":30}'))
M2 = float(input(f'{"Enter grade for Module 2: ":30}'))
M3 = float(input(f'{"Enter grade for Module 3: ":30}'))
M4 = float(input(f'{"Enter grade for Module 4: ":30}'))
M5 = float(input(f'{"Enter grade for Module 5: ":30}'))
M6 = float(input(f'{"Enter grade for Module 6: ":30}'))
GradeList = [M1, M2, M3, M4, M5, M6]

def main():
    print("----------------Results----------------")
    print(f'{"The lowest grade is: ":30}{min(GradeList):.1f}')
    print(f'{"The highest grade is: ":30}{max(GradeList):.1f}')
    print(f'{"The sum of the grades is: ":30}{sum(GradeList):.1f}')
    print(f'{"The average of the grades is: ":30}{sum(GradeList)/len(GradeList):.2f}')
    print("---------------------------------------")

main()