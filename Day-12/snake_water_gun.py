import random
count = 0
user_score = 0
computer_score = 0

while count < 5:
    computer = random.choice(["snake","water","Gun"]).lower()
    user = input("Entre Your Choice : Snake , water , Gun  = ").lower()

    if(user=="snake" and computer=="water"):
        print(f'''
user choose = {user}
computer choose = {computer}
        ''')
        user_score +=1
        print("User Won The Game !")

    elif(user=="water" and computer=="snake"):
        print(f'''
user choose = {user}
computer choose = {computer}
        ''')
        computer_score +=1
        print("Computer Won The Game !")

    elif(user=="snake" and computer=="gun"):
        print(f'''
user choose = {user}
computer choose = {computer}
        ''')
        computer_score +=1
        print("computer Won The Game !")

    elif(user=="gun" and computer=="snake"):
        print(f'''
user choose = {user}
computer choose = {computer}
        ''')
        user_score +=1
        print("user Won The Game !")

    elif(user=="gun" and computer=="water"):
        print(f'''
user choose = {user}
computer choose = {computer}
        ''')
        computer_score +=1
        print("computer Won The Game !")

    elif(user=="water" and computer=="gun"):
        print(f'''
user choose = {user}
computer choose = {computer}
        ''')
        user_score +=1
        print("user Won The Game !")

    elif(user=="water" and computer=="water" or user=="gun" and computer=="gun"  or user=="snake" and computer=="snake"):
        print(f'''
user choose = {user}
computer choose = {computer}
        ''')
        print(" Game Draw!")

    else:
        print("Invalid Input !")  

    count += 1   




print(f'''
user Total score = {user_score}
computer Total score = {computer_score}
''')

if (user_score>computer_score):
    print("User won the Game !")

else:
     print("Computer won the Game !")

        















    

