class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(self.name, "says Woof Woof!")


d1 = Dog("Tommy", "Labrador")
d1.bark()