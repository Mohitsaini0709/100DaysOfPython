class Order:

    def __init__(self, food, quantity, price):
        self.food = food
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        total = self.quantity * self.price
        print("Food:", self.food)
        print("Total Bill:", total)


o1 = Order("Pizza", 2, 250)
o1.total_bill()