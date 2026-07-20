# Create a class named Mobile.

# Requirements
# Create a constructor (__init__) with:
# brand
# model
# price
# Create two methods:
# display() → Print all mobile details.
# call() → Print "Calling..."

class Mobile:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price 

    def display(self):
        print(f"Your Mobile brand Is {self.brand}")
        print(f"Your Mobile Model Is {self.model}")
        print(f"Your Mobile price Is {self.price}")

    def call(self):
        print("Calling...")    

x = Mobile("samsung", 2025,12000)
x.display()
x.call()
