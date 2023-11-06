import sqlite3

class User:
    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name)
        self.c = self.con.cursor()
        self.create_user_table()

    def create_user_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS User (
            user_id INTEGER PRIMARY KEY,
            account_name TEXT,
            account_number INTEGER,
            account_balance REAL,
            manager_id INTEGER
        )''')
        self.con.commit()
    def create_account(self, fullname, account_number, amount, manager_id):
        self.c.execute("INSERT INTO User (account_name, account_number, account_balance, manager_id) VALUES (?, ?, ?, ?)", (fullname, account_number, amount, manager_id))
        self.con.commit()
        print("Your LCM Bank account has been created successfully!")

    def deposit(self, account_number, amount):
        self.c.execute("SELECT account_balance FROM User WHERE account_number=?", (account_number,))
        current_balance = self.c.fetchone()[0]
        new_balance = current_balance + amount
        self.c.execute("UPDATE User SET account_balance=? WHERE account_number=?", (new_balance, account_number))
        self.con.commit()
        print(f"Amount {amount} has been deposited. Your new balance is {new_balance}")

    def withdraw(self, account_number, amount):
        self.c.execute("SELECT account_balance FROM User WHERE account_number=?", (account_number,))
        current_balance = self.c.fetchone()[0]

        if current_balance >= amount:
            new_balance = current_balance - amount
            self.c.execute("UPDATE User SET account_balance=? WHERE account_number=?", (new_balance, account_number))
            self.con.commit()
            print(f"Amount {amount} has been withdrawn. Your new balance is {new_balance}")
        else:
            print("Insufficient funds. Withdrawal cannot be processed.")
