#Christopher Ward
#MPCS 50101, Winter 2015
#Homework 4
#Banking file to be imported by bank_accounts.py

class BankAccount:

    def __init__(self):
        self.my_checking_account = 0
        self.my_savings_account = 0

    def balance(self):
        return self.balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    def withdraw(self, withdraw_amount):
        #offer overdraft protection
        if withdraw_amount <= self.balance:
            self.balance -= withdraw_amount

    def transfer(self, transfer_amount, to_account):
        #overdraft protection in transactions
        if transfer_amount < self.balance:
            self.withdraw(transfer_amount)
            to_account.deposit(transfer_amount)
        else:
            pass

my_checking_account = BankAccount()
my_savings_account = BankAccount()
