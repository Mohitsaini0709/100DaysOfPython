class Student:

    def study(self):
        print("Student is studying.")


class Sports:

    def play(self):
        print("Student is playing Cricket.")


class College(Student, Sports):
    pass


c = College()

c.study()
c.play()