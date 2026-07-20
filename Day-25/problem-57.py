# Create a Student class with:
# Attributes: name, age, marks
# Method: display()

class student:
    name = "Mohit"
    age = 19
    marks = 90
    def std(self):
        print(f"Name = {self.name}")
        print(f"age = {self.age}")
        print(f"marks = {self.marks}")

display = student()    
display.std()