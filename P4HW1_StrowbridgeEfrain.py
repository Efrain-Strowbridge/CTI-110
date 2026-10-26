# Efrain Strowbridge
# 10/26/26
# P4HW1
# This program works just like a grade calculator for teachers.

# This section focuses on inputting the grades and adding each new grade into the list
Amount = int(input("How many scores do you want to input: "))
GradeList = []
print("---------------------------------------")
for score_number in range(1, Amount + 1):
    score = float(input(f"Enter score #{score_number}: "))
    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{score_number} again: "))
    GradeList.append(score)

# This section prints out the list and all needed information for the grades in the list. 
def main():
    ModGradeList = GradeList.copy()
    ModGradeList.remove(min(ModGradeList))
    Grade = sum(ModGradeList)/len(ModGradeList)
    print("----------------Results----------------")
    print(f'{"Lowest Score":20}: {min(GradeList):.1f}')
    print(f'{"Modified List":20}: {ModGradeList}')
    print(f'{"Scores Average":20}: {Grade:.2f}')
    if (Grade >= 90):
        print(f'{"Grade":20}: A')
    elif (Grade >= 80):
        print(f'{"Grade":20}: B')
    elif (Grade >= 70):
        print(f'{"Grade":20}: C')
    elif (Grade >= 60):
        print(f'{"Grade":20}: D')
    else:
        print(f'{"Grade":20}: F')
    print("---------------------------------------")

main()