import random

continue_playing = "yes"

while continue_playing == "yes":
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    question = f"What is {num1} x {num2}?"
    answer = int(input(question))
    if answer == num1 * num2:
        print("Correct!")
    else:
        print("Incorrect!")
    continue_playing = input("Do you want to continue? (yes or no) ")

print("Thank you for taking the quiz!")

