''' 
print this pattern using loop

  *
 ***
*****     
'''

for i in range(3):
    stars = 2 * i + 1
    space = 2 - i 
    print(" "*space + "*" * stars)
