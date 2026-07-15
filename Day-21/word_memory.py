import random
import time

words = [
    "apple",
    "banana",
    "orange",
    "mango",
    "grapes",
    "python",
    "computer",
    "keyboard",
    "monitor",
    "internet",
    "student",
    "teacher",
    "library",
    "football",
    "cricket",
    "elephant",
    "tiger",
    "mountain",
    "river",
    "camera"
]
computer = []
for i in range (5):
   computer.append(random.choice(words))


print("\n Remember This Words : ")
print(computer)
print("You Have 5 sec to remember these words !")
time.sleep(5)

print("\n"*30)

score = 0

for i in range(5):
   guess = input(f"Words No - {i+1} :  ").lower()
   if(computer[i] == guess):
      score += 1


print("\nCorrect Words:", computer)
print("Your Score:", score, "/5")






