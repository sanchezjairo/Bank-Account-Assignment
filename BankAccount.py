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
    
