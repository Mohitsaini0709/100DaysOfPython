# Create a class Bike.
# Attributes
# brand
# model
# price
# Methods
# display()
# increase_price(amount) → Increase the price by the given amount.


class bike:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print(f"Brand = {self.brand}")
        print(f"model = {self.model}")
        print(f"price = {self.price}")

    def increase_price(self, amount):
        self.price += amount
        print(f"Increase the price by the given amount 10,000 and the total amount is . {self.price}")


b1 = bike("Tvs",2007,120000)
b1.increase_price(10000)
b1.display()

