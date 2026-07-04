# Return the maximum number in a list.

list = [4,5,7,9,14,21,32,45,50]


def maxi_num():
    maximum = list[0]
    for num in list:
        if num > maximum:
            maximum = num
    return ("Maximun Number is :", maximum)   

maximun_number = maxi_num()

print(maximun_number)

