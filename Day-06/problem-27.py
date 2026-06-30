# check a student is passes or failed 

a = int(input("Enter Your Engish Mark : "))
b = int(input("Enter Your Hindi Mark : "))
c = int(input("Enter Your Math Mark : "))
d = int(input("Enter Your Physics Mark : "))
e = int(input("Enter Your Chemistry Mark : "))

total = a+b+c+d+e
percentage = (total/500)*100

print(f"Your total percentage is : {percentage}%")

if(percentage>90):
    print("Congratulation You Score Above 90 ")

elif(percentage < 90 and percentage > 33):
    print("Congratulation You passed the Exam ")
    
else:
    print("You Will Failed")    