# Bank-Account-Assignment
# Added so I can make a random number generator
import random 
# Made a class called BankAccount with instance variables and attributes
class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name,
        self.account_number = str(random.randint(100000000,999999999))
        self.routing_number = 475935201
        self.balance = 0
# First method adds the deposit amount and safes it into the instance variable self.balance
    def deposit(self,amount):
        self.balance = amount + self.balance
# I did this so the deposited money can have 2 decimal places
        amount = "{:.2f}".format(self.balance)
        print(f'Amount Deposited:${amount}')
# Second method subtracts your balance with the amount you want and I also added an if conditional so that if you subtracted more than your balance you will get hit with a message and a over draft fee 
    def withdraw(self,amount):
        if amount > self.balance:
            print('Insufficient funds. Overdraft fee will be $10')
            self.balance = self.balance - amount - 10
            amount = "{:.2f}".format(self.balance)
        else:
            self.balance = self.balance-amount
            amount = "{:.2f}".format(self.balance)
            print(f'Amount Withdrawn:${amount}')
# when this method is called it just tells you your balance on your account
    def get_balance(self):
        print(f'Hello good day your balance is ${"{:.2f}".format(self.balance)}')
# this method adds interest to your account that you have to pay every month
    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance = self.balance - interest
# this method works just like a recipt it prints out your name, acc no, routing no, and your balance using the instance variables we created above.       
    def recipt(self):
        self.account_number = (self.account_number[0:4])
        print(f'\n{self.full_name}\n Account No.:****{self.account_number}\n Routing No.:{self.routing_number}\n Balance.:${"{:.2f}".format(self.balance)}\n')
jairo = BankAccount('Jairo sanchez',0,0,0)
jairo.deposit(100)