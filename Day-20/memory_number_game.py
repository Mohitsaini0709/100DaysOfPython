import random
import time


print("="*30 +" GAME  START " + "="*30)

computer = []

for i in range(10):
    computer.append(random.randint(1, 99))

print("\nRemember these numbers:")
print(computer)

print("\nYou have 5 seconds to memorize...")
time.sleep(5)

print("\n" * 30)

print("Now enter the numbers in the same order.\n")

score = 0

for i in range(10):
    guess = int(input(f"Number {i+1}: "))
    if guess == computer[i]:
        score += 1

print("\nCorrect Numbers:", computer)
print("Your Score:", score, "/10")

if score >= 5:
    print("🏆 Excellent!")
elif score == 4 or score  == 3:
    print("👍 Good Job!")
else:
    print("😅 Better Luck Next Time!")