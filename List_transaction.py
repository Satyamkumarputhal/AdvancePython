def login(user_id,password):
    attempts = 3
    authenticated = False

    while attempts > 0:
        login_id = input("Enter User ID: ")
        login_password = input("Enter Password: ")

        if login_id == user_id and login_password == password:
            print("Login successful.\n")
            authenticated = True
            break
        else:
            attempts -= 1
            print(f"Invalid credentials. Attempts left: {attempts}")

    if not authenticated:
        print("Too many failed attempts. Exiting program.")
        exit()

def Deposit(balance):
    amt = int(input("Enter deposit amount: "))
    if amt > 0:
        balance += amt
        transactions.append(f"Deposited {amt} rs.")
    else:
        print("Amount must be positive.")
    return balance

def Withdraw(balance):
    amt = int(input("Enter withdraw amount: "))
    if amt <= 0:
        print("Amount must be positive.")
    elif amt <= balance:
        balance -= amt
        transactions.append(f"Withdrawn {amt} rs.")
    else:
        print("Low balance.")
    return balance


def check_balance(balance):
    print("Available balance:", balance)

def Transsaction_hist(transactions):
    if transactions:
        for t in transactions:
            print(t)
    else:
        print("No transaction found.") 
    

#Transaction system
print("=== User Registration ===")
user_id = input("Set User ID: ")
password = input("Set Password: ")

print("\nRegistration successful. Please log in.\n") 

login(user_id,password)

balance = 0
transactions = []    
while True:
    print("\nEnter your choice:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Transaction history")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
       balance = Deposit(balance)

    elif choice == 2:
        balance = Withdraw(balance)

    elif choice == 3:
        check_balance(balance)

    elif choice == 4:
        Transsaction_hist(transactions) 

    elif choice == 5:
        print("Thank you for using transaction system.")
        break

    else:
        print("Enter a valid choice.")
