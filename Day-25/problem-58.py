# Create a class named Car.
# Requirements:
# Create a constructor (__init__) with:
# brand
# model
# color
# Create two methods:
# start() → Print "Car Started"
# display() → Print all car details.
# Create 2 objects with different values.


class car:
    brand = "Maruti Shizuki"
    model = 2014
    color = "Black"
    def __init__(self):
        print(f"This Car Brand Is {self.brand} and model is {self.model} and color is {self.color}")
    def start(self):
        print("Car started")   

display = car()
display.start()         