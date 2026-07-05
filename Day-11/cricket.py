import random

print('''\n🏏 Rule:Choose a number between 1 and 6. If your number matches the computer's number, you're OUT! Otherwise, your chosen number is added to your score. Keep scoring until you're out! and if you print invalid number then you will out ! \n''')

print("Game Start...\n")
print("User Won The Toss ! User Choose Batting!")

computer_score = 0
user_score = 0

while True:
    computer = random.randint(1,6)
    user = int(input("Entre a number between 1-6 : "))
    
    if(user>6 or user<1):
        print("Invalid Number!")
        break

    elif(user!=computer): 
        user_score += user
        print(f'''
user-choice = {user}
Computer choice = {computer}
''')

    else:
        print(f'''
user-choice = {user}
Computer choice = {computer}
''')
        print("OUT!")
        break 
        
print(f"Your Total Score : {user_score}\n") 


print("........ Now Computer Batting Start.......")

while True:
    computer = random.randint(1,6)
    user = int(input("Entre a number between 1-6 : "))
    if(user>6 or user<1):
        print("Invalid Number!")
        break
    elif(user!=computer): 
        computer_score += computer
        print(f'''
Computer choice = {computer}
user-choice = {user}
''')
    else:
        print(f'''
Computer choice = {computer}              
user-choice = {user}
''')
        print("OUT!")
        break 

if(user_score>computer_score):
    print(f'''
Computer Total Score = {computer_score}
user Total Score = {user_score}

user won the Game
''')
    
else:
     print(f'''
Computer Total Score = {computer_score}
user Total Score = {user_score}

Computer won the Game
''')

    
    
    



