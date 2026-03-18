# Question 3: Bank Account Operations

# Q.
# Design a class BankAccount with the following members:

# account_holder

# balance

# Include member functions:

# deposit(amount) to add money

# withdraw(amount) to withdraw money only if sufficient balance is available

# Create an object and demonstrate both deposit and withdrawal operations.

class bank_account:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print("Updated Balance:", self.balance)
    
    def withraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Updated Balance: ", self.balance)
        else: 
            print("Insufficient balance")

acc = bank_account("Neha", 4000)
acc.deposit(1500)
acc.withraw(7000)
