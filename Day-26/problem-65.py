class BankAccount:

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def display(self):
        print("Holder:", self.holder)
        print("Balance:", self.balance)


b1 = BankAccount("Mohit", 5000)
b1.deposit(2000)
b1.display()