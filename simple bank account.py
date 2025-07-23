from abc import ABC, abstractmethod
import csv

class Bank(ABC):
    def __init__(self, name, password, balance):
        self.name = name
        self.__password = password
        self._balance = balance

    
    def deposit(self, amount):
        pass

   
    def withdraw(self, amount):
        pass

    def show_balance(self):
        print(f"{self.name} | Balance: ₹{self._balance}")

    def check_password(self, pw):
        return self.__password == pw

    def to_dict(self):
        return {
            "name": self.name,
            "password": self.__password,
            "balance": self._balance,
            "type": self.__class__.__name__
        }
class SalaryAccount(Bank):
    def deposit(self, amount):
        self._balance += amount
        print(f" Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient balance")

class SavingsAccount(Bank):
    min_balance = 1000

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if self._balance - amount >= SavingsAccount.min_balance:
            self._balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print(f"Minimum balance ₹{SavingsAccount.min_balance} required")
def save_accounts(accounts, filename="accounts.csv"):
    with open(filename, "w", newline="") as f:
        fieldnames = ["name", "password", "balance", "type"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for acc in accounts:
            writer.writerow(acc.to_dict())

def load_accounts(filename="C:\\Users\\V&V\\Documents\\python lb\\exx.csv"):
    accounts = []
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                name, pwd = row["name"], row["password"]
                bal = float(row["balance"])
                typ = row["type"]
                if typ == "SalaryAccount":
                    accounts.append(SalaryAccount(name, pwd, bal))
                else:
                    accounts.append(SavingsAccount(name, pwd, bal))
    except FileNotFoundError:
        pass
    return accounts
filename="C:\\Users\\V&V\\Documents\\python lb\\exx.csv"
accounts = load_accounts(filename)

while True:
    print("\n---Welcome to Mini Bank ---")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")
    ch = input("Choose: ")

    if ch == "1":
        name = input("Enter name: ")
        pwd = input("Set password: ")
        bal = float(input("Initial deposit: "))
        acc_type = input("Account Type (salary/savings): ").lower()
        if acc_type == "salary":
            acc = SalaryAccount(name, pwd, bal)
        else:
            acc = SavingsAccount(name, pwd, bal)
        accounts.append(acc)
        save_accounts(accounts, filename)
        print("Account created and saved!")

    elif ch == "2":
        name = input("Enter name: ")
        pwd = input("Enter password: ")
        user = None
        for a in accounts:
            if a.name == name and a.check_password(pwd):
                user = a
                break
        if user:
            print(f"Welcome {user.name}!")
            while True:
                print("\n1. Deposit\n2. Withdraw\n3. Balance\n4. Logout")
                act = input("Choose: ")
                if act == "1":
                    amt = float(input("Amount: "))
                    user.deposit(amt)
                elif act == "2":
                    amt = float(input("Amount: "))
                    user.withdraw(amt)
                elif act == "3":
                    user.show_balance()
                elif act == "4":
                    print("Logged out")
                    save_accounts(accounts,filename)
                    break
        else:
            print("Wrong credentials!")

    elif ch == "3":
        save_accounts(accounts,filename)
        print("Exiting. Thank you!")
        break
