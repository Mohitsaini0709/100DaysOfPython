
class subject:
    def __init__(self,name,teacher,semester):
        self.name = name
        self.teacher = teacher
        self.semester = semester
    def display(self):
        print("\n","Subject:", self.name)
        print("Teacher:", self.teacher)
        print("Semester:", self.semester,"\n")

name = input("Enter Subject Name: ")
teacher = input("Enter Teacher Name: ")
semester = int(input("Enter Semester: "))

s1 = subject(name, teacher, semester)
s1.display()
