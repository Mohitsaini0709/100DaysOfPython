class BankAccount:

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def show_balance(self):
        print("Account Holder:", self.holder)
        print("Balance:", self.balance)


b1 = BankAccount("Mohit", 10000)
b1.show_balance()