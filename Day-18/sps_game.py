import random

stone = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
computer = random.choice(["Stone" , "paper", "scissor"]).lower()
user = input("Entre Your Choice : ").lower()

print("Computer Choice is :")
match computer:
    case "stone":
        print(stone)
    case "paper":
        print(paper)
    case "scissor":
        print(scissor)

print("User Choice is :")
match user:
    case "stone":
        print(stone)
    case "paper":
        print(paper)
    case "scissor":
        print(scissor)
    case _:
        print("Invalid Choice")   



if (computer == user ):
    print("Match Draw !")
elif(computer == "scissor" and user == "paper"):    
    print(f"Computer Won The Match")
    print(f"Computer choose : {computer}")
elif(computer == "scissor" and user == "stone"):    
    print(f"user Won The Match")
    print(f"user choose : {user}")
elif(computer == "paper" and user == "stone"):    
    print(f"Computer Won The Match")
    print(f"Computer choose : {computer}")
elif(computer == "paper" and user == "scissor"):    
    print(f"user Won The Match")
    print(f"user choose : {user}")
elif(computer == "stone" and user == "scissor"):    
    print(f"Computer Won The Match")
    print(f"Computer choose : {computer}") 
elif(computer == "stone" and user == "paper"):    
    print(f"user Won The Match")
    print(f"user choose : {user}")       
