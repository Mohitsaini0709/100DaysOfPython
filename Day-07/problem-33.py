# Reverse a number using for loop.

num = input("Enter a number: ")
rev = ""

for i in num:
    rev = i + rev 

print (rev)