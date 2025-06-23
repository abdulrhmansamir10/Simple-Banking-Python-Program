accounts = {}
current_user = None

def create_account():
    username = input(f"Enter your username")
    if username in accounts:
        print("this account already existed")
    else:
        password = input(f"Enter a 5 unique digits  password: ")
        accounts[username]= {
            "password": password,
            "balance": 0.0
        }
        print("Account created successfully")
def login():
    global current_user
    username = input(f"Enter your username.")
    password = input(f"Enter your password.")
    if username in accounts and accounts[username]["password"] == password:
        current_user = username
        print(f"welcome back; {username}")
    else:
        print(f"Invalid username or password")
    
def show_balance():
    if current_user:
        print(f"Your balance is {accounts[current_user]['balance']}")
    else:
        print("You must login first")

def deposit():
    if current_user:
        amount = float(input(f"enter your amount"))
        if amount <= 0:
            print("You must enter a positive amount.")
        else:
            accounts[current_user]['balance'] =+ amount
            print(f"${amount:.2f} deposited")
    
    else:
        print("You must login first")

def withdraw():
    if current_user:
        amount = float(input(f"Enter amount to be withdrawn"))
        if amount <= 0:
            print("You must enter a positive number")
        elif amount > accounts[current_user]['balance']:
            print("Insufficient amount")
        else:
            accounts[current_user]['balance'] -= amount
            print("${amount:.2f} withdrawn")
    else:
        print("You must login first")
    

    

#global variables
program_is_running = True

while program_is_running:
    print("\n---- Banking Program ----")
    print("1. Create Account")
    print("2. Log In")
    print("3. Show Balance")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Exit")

    choice = input("Choose the prosedure you want to use from (1-6): ")
    if choice == "1":
        create_account()
    elif choice == "2":
        login()
    elif choice == "3":
        show_balance()
    elif choice == "4":
        deposit()
    elif choice == "5":
        withdraw()
    elif choice == "6":
        program_is_running = False
        print("See You Soon")
    else:
        print("You entered an Invalid Choice.")
print(f"Thank you for Using this simple Banking Program")

