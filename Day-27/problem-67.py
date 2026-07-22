# Create a class Bottle.
# Attributes
# brand
# capacity (in ml)
# water_level (current water in the bottle)
# Methods
# fill()
# Fill the bottle completely.
# Set water_level = capacity.
# drink(amount)
# Reduce the water level by the given amount.
# display()

# Print:

class bottle:
    def __init__(self,brand,capacity,water_level):
        self.brand = brand
        self.capacity = capacity
        self.water_level = water_level

    def display(self):
        print(f"Brand = {self.brand}")    
        print(f"capacity = {self.capacity}ml")    
        print(f"water_level = {self.water_level}ml")  

    def set_level(self,user):
        user  +=  self.water_level
        if user > 1000:
            print(f"Water Overflow Because Total limit of bottle is 1000 ml and yo fill total {user}")
        else :
            print(f"\n water_level = {user}ml") 
        print(f"water_level Updated !")
         

b1 = bottle("Milton",1000,700) 
b1.display()
b1.set_level(100)
     