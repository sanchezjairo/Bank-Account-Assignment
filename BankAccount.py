import random 

class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name,
        self.account_number = str(random.randint(100000000,999999999))
        self.routing_number = 475935201
        self.balance = 0
    def deposit(self,amount):
        self.balance = amount + self.balance
        amount = "{:.2f}".format(self.balance)
        print(f'Amount Deposited:{amount}')
    def withdraw(self,amount):
        if amount > self.balance:
            print('Insufficient funds. Overdraft fee will be $10')
            self.balance = self.balance - amount - 10
            amount = "{:.2f}".format(self.balance)
        else:
            self.balance = self.balance-amount
            amount = "{:.2f}".format(self.balance)
            print(f'Amount Withdrawn:{amount}')
    def get_balance(self):
        print(f'Hello good day your balance is {"{:.2f}".format(self.balance)}')

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance = self.balance - interest
        
    def recipt(self):
        self.account_number = (self.account_number[0:4])
        print(f'\n{self.full_name}\n Account No.:****{self.account_number}\n Routing No.:{self.routing_number}\n Balance.:{"{:.2f}".format(self.balance)}\n')