class Calculator:

    @staticmethod
    def add(a, b):
        return a + b
    def sub(a, b):
        return a - b
    def multi(a, b):
        return a * b
    def devide(a, b):
        return a / b

print(Calculator.add(10, 20))
print(Calculator.sub(10, 20))
print(Calculator.multi(10, 20))
print(Calculator.devide(10, 20))