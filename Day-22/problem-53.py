# Write a function that returns the second largest unique number from a list.

list = [10,20,50,30,40,80,90,60,100,70 ,99]

def sec_large_num():
    list.sort()
    return list[-2]
x = sec_large_num()
print(f"second largest number in a list is {x}")

