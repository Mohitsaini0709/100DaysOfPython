# Dog ki information:
# Name
# Breed
# Age

class dog:
    def __init__(self,name,breed,age):
        self.name = name 
        self.breed = breed
        self.age = age 

    def display(self):
        print(f"My Dog Name is {self.name},My Dog Breed Is {self.breed},And My Dog Age Is {self.age}")

a = dog("Charlie" , "Shih Tzu" , 2)
a.display()        