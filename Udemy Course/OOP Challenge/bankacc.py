class BankAccount:


    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'Name: {self.name}\nBalance: {self.balance}'

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} has been added to {self.name}'s account.\nCurrent Balance: ${self.balance}")
    
    def withdraw(self, amount):
        if self.balance - amount < 0:
            print(f'Your balance is: ${self.balance}. you do not have enough money to withdraw ${amount}.')
        else:
            self.balance -= amount
            print(f'Succesfully withdrawn ${amount}.')
    

my_acc = BankAccount('Ahanaf', 100)
while True:
    decision = input('Deposit, Withdraw or Info? (d/w/i): ').lower()
    if decision == 'd':
        dep_amount = int(input('Amount: '))
        my_acc.deposit(dep_amount)
    elif decision == 'w':
        with_amount = int(input('Amount: '))
        my_acc.withdraw(with_amount)
    elif decision == 'i':
        print(my_acc)
    else:
        print('That is not a valid option.')


