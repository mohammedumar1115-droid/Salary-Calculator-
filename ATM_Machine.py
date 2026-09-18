# PROJECT 3 - Simple ATM Machine
print("--- WELCOME TO UMAR'S ATM ---")

balance = 125000
pin = 5467

entered_pin = int(input("Enter your 4-digit PIN: "))

if entered_pin == pin:
    print("PIN Correct! Your balance is:", balance)
    
    amount = int(input("Enter amount to withdraw: "))
    
    if amount <= balance:
        balance = balance - amount
        print("Withdraw Successful!")
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance!")
else:
    print("Wrong PIN! Access Denied")
