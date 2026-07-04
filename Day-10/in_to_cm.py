def inch_to_cm():
    inch = float(input("Enter the length in inches: "))
    cm = inch*2.54
    return (f"{inch} inch have {cm} centimeter")

output = inch_to_cm()

print(output)