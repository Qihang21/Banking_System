class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name 
        self.balance = balance
    
    def store_info(self):
        return {"name": self.name, "balance": self.balance}

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount 
            return True 
        return False 

    def withdraw(self, amount):
        if 0 < amount and amount <= self.balance:
            self.balance -= amount 
            return True 
        return False

    def transfer(self, recipient, amount):
        if self.withdraw(amount):
            recipient.deposit(amount)
            return True 
        return False 
    
    def show_balance(self):
        return f"Acount: {self.name}, Balance: {self.balance:.2f}"
    