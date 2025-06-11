'''from auth import register_user, login
from transactions import deposit, withdraw, transfer
from admin_panel import view_all_users, freeze_account, activate_account  # updated

def start():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        ch = input("Enter choice: ")
        if ch == '1':
            name = input("Name: ")
            email = input("Email: ")
            pwd = input("Password: ")
            register_user(name, email, pwd)

        elif ch == '2':
            email = input("Email: ")
            pwd = input("Password: ")
            user = login(email, pwd)
            if user:
                if user['role'] == 'admin_panel':  # updated role check
                    admin_panel_menu()  # updated function
                else:
                    user_menu(user['id'])

        elif ch == '3':
            break

def user_menu(uid):
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Transfer\n4. Logout")
        ch = input("Choice: ")
        if ch == '1':
            amt = float(input("Amount: "))
            deposit(uid, amt)
        elif ch == '2':
            amt = float(input("Amount: "))
            withdraw(uid, amt)
        elif ch == '3':
            email = input("To Email: ")
            amt = float(input("Amount: "))
            transfer(uid, email, amt)
        elif ch == '4':
            break

def admin_panel_menu():  # renamed function
    while True:
        print("\n1. View Users\n2. Freeze Account\n3. Activate Account\n4. Logout")
        ch = input("Choice: ")
        if ch == '1':
            view_all_users()
        elif ch == '2':
            email = input("Email to freeze: ")
            freeze_account(email)
        elif ch == '3':
            email = input("Email to activate: ")
            activate_account(email)
        elif ch == '4':
            break

if __name__ == "__main__":
    start()
'''
from auth import register_user, login_user
from transactions import deposit, withdraw, transfer, view_transactions

def start():
    print("🏦 Welcome to Python Bank!")
    print("1. Register")
    print("2. Login")
    choice = input("Choice: ")

    if choice == '1':
        name = input("Name: ")
        email = input("Email: ")
        pwd = input("Password: ")
        register_user(name, email, pwd)
        start()

    elif choice == '2':
        email = input("Email: ")
        pwd = input("Password: ")
        user = login_user(email, pwd)

        if user:
            user_panel(user)
        else:
            print("❌ Login failed.")
            start()
    else:
        print("❌ Invalid choice.")
        start()

def user_panel(user):
    print(f"\n👋 Welcome, {user[1]} ({user[3]})")  # (id, name, password, email)
    
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Check Balance")
        print("5. View Transactions")
        print("6. Logout")
        choice = input("Choice: ")

        if choice == '1':
            amount = float(input("Amount: "))
            deposit(user[0], amount)

        elif choice == '2':
            amount = float(input("Amount: "))
            withdraw(user[0], amount)

        elif choice == '3':
            to_email = input("Transfer to (email): ")
            amount = float(input("Amount: "))
            transfer(user[0], to_email, amount)

        elif choice == '4':
            from transactions import get_balance
            balance = get_balance(user[0])
            print(f"💼 Current balance: ₹{balance:.2f}")

        elif choice == '5':
            view_transactions(user[0])

        elif choice == '6':
            print("👋 Logged out successfully.")
            break

        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    start()
