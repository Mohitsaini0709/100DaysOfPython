while True:
    a = int(input("Entre Your 1st Number : "))
    b = int(input("Entre Your 2nd Number : "))

    sym = input("Entre symbol here ( + , - , / , % , * ) : ")

    if sym == "+":
        print(a+b)
    elif sym == "-":
        print(a-b)
    elif sym == "*":
        print(a*b)
    elif sym == "/":
        print(a/b)
    elif sym == "%":
        print(a%b)
    else:
        print("Invalid Input !")
        break