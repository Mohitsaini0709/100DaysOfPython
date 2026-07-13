import random

secret = random.randint(1, 1000)
count = 0

print("Number Guessing Game")
print("Guess the number between 1 and 1000")

while True:
    guess = int(input("Enter your guess: "))
    count += 1

    if guess < secret:
        print("Higher!")
    elif guess > secret:
        print("Lower!")
    else:
        print("\n🎉 Congratulations! You guessed the correct number.")
        print("Secret Number:", secret)
        print("Total Attempts:", count)
        break