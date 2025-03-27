import os
import csv 
from bank_account import BankAccount

class BankingSystem:
    def __init__(self):
        self.accounts = {}
    
    def save_accounts(self):
        accounts_data = {account.name: account for account in self.accounts.values()}
        existing_data = {}

        try:
            if os.path.exists("bank_account.csv"):
                with open("bank_account.csv", "r", newline = "") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        existing_data[row["name"]] = BankAccount(row["name"], float(row["balance"]))
        
            existing_data.update(accounts_data)

            with open("bank_account.csv", "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["name", "balance"])
                writer.writeheader()
                for account in existing_data.values():
                    writer.writerow(account.store_info())
        except FileNotFoundError:
            print("save_accounts(): The csv file doesn't exist.")

    def get_account(self, name):
        try:
            if os.path.exists("bank_account.csv"):
                with open("bank_account.csv", "r") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        if row["name"] == name:
                            account = BankAccount(row["name"], float(row["balance"]))
                            self.accounts[name] = account 
                            return account 
        except FileNotFoundError:
            print("get_account(): The csv file doesn't exist.")

    def create_account(self):
        name = input("Create a new account name: ")
        account = self.get_account(name)
        if account:
            print("The account name has already exists.")
            return False 
        
        while True:
            try:
                balance = float(input("Enter initial balance: "))
                if balance < 0:
                    print("The initial balance cannot be negative. Please enter the value again.")
                else:
                    break
            except ValueError:
                print("create_account(): Invalid input.Please enter a numeric balance value.")

        self.accounts[name] = BankAccount(name, balance)
        self.save_accounts()
        print("New account created successfully")
        return True 

    def deposit_money(self):
        name = input("Enter account name: ")
        account = self.get_account(name)
        if account:
            while True:
                amount = input("Enter amount to deposit: ")
                try:
                    amount = float(amount)
                    if amount <= 0:
                        print("Amount must be greater than zero. Please try enter again.")
                    else:
                        break 
                except ValueError:
                    print("deposit_money(): Invalid input. Please enter a numeric value.")

            if account.deposit(amount):
                self.save_accounts()
                print("Deposit Successfully")
            else:
                print("Invalid deposit amount.")
        else:
            print("Account not found.")

    def withdraw_money(self):
        name = input("Enter account name: ")
        account = self.get_account(name)
        if account:
            while True:
                amount = input("Enter amount to withdraw: ")
                try:
                    amount = float(amount)
                    if amount <= 0:
                        print("Amount must be greater than zero. Please try enter again.")
                    else:
                        break 
                except ValueError:
                    print("withdraw_money(): Invalid input. Please enter a numeric value.")

            if account.withdraw(amount):
                self.save_accounts()
                print("Withdraw successful.")
            else:
                print("Insufficient balance or invalid amount.")
        else:
            print("Account not found.")

    def transfer_money(self):
        sender_name = input("Enter sender's account name: ")
        recipient_name = input("Enter recipient's account name: ")

        while True:
            amount = input("Enter amount to transfer: ")
            try:
                amount = float(amount)
                if amount <= 0:
                    print("Amount must be greater than zero. Please try enter again.")
                else:
                    break 
            except ValueError:
                print("transfer_money(): Invalid input. Please enter a numeric value.")

        sender = self.get_account(sender_name)
        recipient = self.get_account(recipient_name)

        if sender and recipient:
            if sender.transfer(recipient, amount):
                self.save_accounts()
                print("Transfer successful.")
            else:
                print("Insufficient funds.")
        else:
            print("One or both accounts do not exist.")

    def check_balance(self):
        name = input("Enter account name: ")
        account = self.get_account(name)
        if account:
            print(account.show_balance())
        else:
            print("This account doesn't exist.")

    def download_accounts(self):
        try:
            with open("bank_account.csv", "rb") as source_file:  
                with open("download_bank_account.csv", "wb") as dest_file:  
                    dest_file.write(source_file.read())
            
            print(f"Download your file here: download_bank_account.csv")
        except FileNotFoundError:
            print("download_accounts(): The file csv doesn't exist.")
