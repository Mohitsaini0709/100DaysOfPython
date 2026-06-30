# write a program to find the greatest number entred by the user.

a = int(input("Enter Your 1st Number : "))
b = int(input("Enter Your 2nd Number : "))
c = int(input("Enter Your 3rd Number : "))
d = int(input("Enter Your 4th Number : "))

if(a>b and a>c and a>d):
    print(f"Your 1st number {a} is greator")
elif(b>a and b>c and b>d):
    print(f"Your 2ns number {b} is greator")
elif(c>a and c>b and a>d):
    print(f"Your 3rd number {c} is greator")
else:
    print(f"Your 4th number {d} is greator")
