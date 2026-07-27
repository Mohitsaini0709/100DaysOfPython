class Teacher:

    def teach(self):
        print("Teaching Students")


class Singer:

    def sing(self):
        print("Singing Song")


class Person(Teacher, Singer):
    pass


p = Person()

p.teach()
p.sing()