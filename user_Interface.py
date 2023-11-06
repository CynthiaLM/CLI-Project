from user import User
from account_manager import AccountManager

class UserInterface:
    def __init__(self, db_name):
        self.user = User(db_name)
        manager_name = input("Enter the Account Manager's Full Name: ").upper()
        self.account_manager = AccountManager(manager_name)    
    def user_menu(self):
        while True:
            print("\nUser Menu:")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter your choice (1/2/3/4): ")

            if choice == "1":
                fullname = input("Enter Your Full Name: ").upper()
                account_number = int(input("Enter your account number: "))
                amount = float(input("Enter the initial amount: "))
                manager_id = int(input("Enter your account manager's ID: "))
                self.user.create_account(fullname, account_number, amount, manager_id)
            elif choice == "2":
                account_number = int(input("Enter your account number: "))
                amount = float(input("Enter the amount you want to deposit: "))
                self.user.deposit(account_number, amount)
            elif choice == "3":
                account_number = int(input("Enter your account number: "))
                amount = float(input("Enter the amount you want to withdraw: "))
                self.user.withdraw(account_number, amount)
            elif choice == "4":
                print("Thank you for using LCM Bank. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose 1, 2, 3, or 4.")

    def account_manager_menu(self):
        while True:
            print("\nAccount Manager Menu:")
            print("1. Create Account Manager")
            print("2. Add User")
            print("3. Remove User")
            print("4. View Users")
            print("5. Exit")

            choice = input("Enter your choice (1/2/3/4/5): ")

            if choice == "1":
                manager_name = input("Enter Account Manager's Full Name: ").upper()
                self.account_manager.create_account_manager(manager_name)
            elif choice == "2":
                fullname = input("Enter User's Full Name: ").upper()
                account_number = int(input("Enter user's account number: "))
                amount = float(input("Enter the initial amount: "))
                manager_id = int(input("Enter your account manager's ID: "))
                self.account_manager.add_user(fullname, account_number, amount, manager_id, db_name)
            elif choice == "3":
                user_id = int(input("Enter the user's ID to remove: "))
                self.account_manager.remove_user(user_id)
            elif choice == "4":
                manager_id = int(input("Enter your account manager's ID: "))
                self.account_manager.view_users()
            elif choice == "5":
                print("Thank you for using LCM Bank. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    db_name = "Bank.db"
    user_interface = UserInterface(db_name)

    while True:
        print("\nMain Menu:")
        print("1. User Menu")
        print("2. Account Manager Menu")
        print("3. Exit")

        main_choice = input("Enter your choice (1/2/3): ")

        if main_choice == "1":
            user_interface.user_menu()
        elif main_choice == "2":
            user_interface.account_manager_menu()
        elif main_choice == "3":
            print("Thank you for using LCM Bank. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
