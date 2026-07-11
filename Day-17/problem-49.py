# Write a program that takes a number (1–7) and prints the corresponding day.

day = int(input("Enter day number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thrusday")
    case 5:
        print("Friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("invalid input !")