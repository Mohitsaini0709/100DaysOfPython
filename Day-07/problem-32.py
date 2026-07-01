# check a number is prime or not ?

a = int(input("Enter a number : "))

for i in range (2,a):
    if(a%i) == 0:
        print("These Given Number Is NOt Prime")
        break
else:
    print("These Number Is Prime ")    