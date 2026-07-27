# Class Child(Father, Mother)
# Create an object and call both methods.

class father:
    def bike(self):
        b1 = "TVS"
        print(f"My Father have a {b1} bike")
class mother:
    def car(self):
        c1 = "Swift"
        print(f"My Father have a {c1} car")

class family(father , mother ):
    pass


a = family()
a.bike()
a.car()        

