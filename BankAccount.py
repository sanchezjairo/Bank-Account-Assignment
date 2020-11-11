import random 

# mylist = [1,2,3,4,5,6,7,8,9,10]
# x = random.sample(mylist,9) 
# convert the number to str then slice
class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name,
        self.account_number = random.randint(100000000,999999999)
        self.routing_number = 475935201
        self.balance = 0
    def deposit(self,amount):
        self.balance = amount + self.balance
        amount = "{:.2f}".format(self.balance)
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
        self.balance = self.balance + interest
    def recipt(self):
        print(f'\n{self.full_name}\n Account No.:{self.account_number}\n Routing No.:{self.routing_number}\n Balance.:{self.balance}\n')
jairo = BankAccount('mike sanchez' ,0,0,0)
jairo.deposit(200)
jairo.recipt()