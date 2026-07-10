marks = 0

with open("quiz.txt", "r") as file:
    for question in file:
        question, correct_answer = question.strip().split("|")

        answer = input(question + "\nYour Answer: ")

        if answer.lower() == correct_answer.lower():
            marks += 1
            print("Correct!\n")
        else:
            print("Wrong!")
            print("Correct Answer:", correct_answer)
            print()

print(f"Your total marks is {marks} out of 10.")