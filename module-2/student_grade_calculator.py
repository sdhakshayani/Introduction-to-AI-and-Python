print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")

mark1 = int(input("Enter marks for Subject 1: "))
mark2 = int(input("Enter marks for Subject 2: "))
mark3 = int(input("Enter marks for Subject 3: "))
mark4 = int(input("Enter marks for Subject 4: "))
mark5 = int(input("Enter marks for Subject 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
percentage = total / 5

if mark1 < 35 or mark2 < 35 or mark3 < 35 or mark4 < 35 or mark5 < 35:
    grade = "F"
    result = "Fail"
elif percentage >= 90:
    grade = "A+"
    result = "Pass"
elif percentage >= 80:
    grade = "A"
    result = "Pass"
elif percentage >= 70:
    grade = "B"
    result = "Pass"
elif percentage >= 60:
    grade = "C"
    result = "Pass"
elif percentage >= 50:
    grade = "D"
    result = "Pass"
else:
    grade = "E"
    result = "Pass"

print("\n===== RESULT =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Result:", result)
