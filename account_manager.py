import sqlite3
from user import User 

class AccountManager:
    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name)
        self.c = self.con.cursor()
        self.c.execute('''
            CREATE TABLE User (
                id INTEGER PRIMARY KEY,
                fullname TEXT,
                account_number TEXT,
                amount REAL,
                manager_id INTEGER
            )
        ''')
        self.con.commit()
    def add_user(self, fullname, account_number, amount, manager_id, db_name):
        user = User(db_name) 
        user.create_account(fullname, account_number, amount, manager_id)

    def remove_user(self, account_number):
        self.c.execute("DELETE FROM User WHERE account_number=?", (account_number,))
        self.con.commit()
        print(f"User with account number {account_number} has been removed from the database.")

    def view_users(self):
        self.c.execute("SELECT * FROM User")
        users = self.c.fetchall()
        for user in users:
            print(user)