# Calculator with Exception Handling

try:
    a = int(input("Entre a number :"))
    b = int(input("Entre a number :"))
    symbol = input("Entre Your Symbol Here (+ , - , * , / )")
    if symbol == "+":
        print(a+b)
    elif symbol == "-":
        print(a-b)
    if symbol == "*":
        print(a*b)
    if symbol == "/":
        print(a/b)
except:
    print("Cannot divide by zero. or Enter numbers only.")