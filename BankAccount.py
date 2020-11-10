import random

mylist = [1,2,3,4,5,6,7,8,9,10]
x = random.sample(mylist,9) 
class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name,
        self.account_number = x
        self.routing_number = 890652341,
        self.balance = 0
    def deposit(self,amount):
        self.balance = amount + self.balance
        print(f'Amount Deposited:{amount}')
    def withdraw(self,amount):
        if amount > self.balance:
            print('Insufficient funds.')
            self.balance = self.balance - amount - 10
        else:
            print(f'Amount Withdrawn:{amount}')
    def get_balance(self):
        print(f'Hello good day your balance is {self.balance}')
        return self.balance
    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance + interest
 
