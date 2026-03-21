# if condition1:
#     statement1
# elif condition2:
#     statement2
# else:
#     statement3


marks = int(input("Enter marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"

print("Grade =", grade)
