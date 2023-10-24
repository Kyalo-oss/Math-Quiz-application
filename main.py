import random

continue_playing = "yes"

while continue_playing == "yes":
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    operation = random.choice(["+", "-", "x", "/"])
    if operation == "+":
        question = f"What is {num1} + {num2}?"
        answer = num1 + num2
    elif operation == "-":
        question = f"What is {num1} - {num2}?"
        answer = num1 - num2
    elif operation == "x":
        question = f"What is {num1} x {num2}?"
        answer = num1 * num2
    else:
        question = f"What is {num1} / {num2}?"
        answer = num1 / num2
    user_answer = float(input(question))
    if user_answer == answer:
        print("Correct!")
    else:
        print("Incorrect!")
    continue_playing = input("Do you want to continue? (yes or no) ")

print("Thank you for taking the quiz!")



