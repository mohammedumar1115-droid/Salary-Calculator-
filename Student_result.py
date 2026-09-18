# PROJECT 2 - Student Result Checker
print("--- STUDENT RESULT ---")

name = input("Enter student name: ")
marks = int(input("Enter marks out of 100: "))

if marks >= 50:
    print("Result: PASS")
else:
    print("Result: FAIL")

if marks >= 80:
    print("Grade: A - Excellent!")
elif marks >= 75:
    print("Grade: B - Good Job!")
elif marks >= 60:
    print("Grade: C - Keep Improving")
else:
    print("Grade: D - Need Hard Work")

print("----------------------")
print("Student:", name, "| Marks:", marks)
