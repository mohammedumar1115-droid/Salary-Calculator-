print("--- SALARY CALCULATOR ---")
name = input("Enter your name: ")
salary = int(input("Enter your basic salary: "))
bonus = 0
if salary > 20000:
    bonus = 3000
    print("You get bonus of 3000!")
else:
    print("No bonus, work hard next month")
total = salary + bonus
print("-------- SLIP --------")
print("Name:", name)
print("Basic Salary:", salary)
print("Bonus:", bonus)
print("Total Salary:", total)
