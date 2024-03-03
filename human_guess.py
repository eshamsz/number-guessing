from random import randint

computer_number = randint(1,100)

human_guess = '' #initialize variable

while human_guess != computer_number:
    human_guess = int(input("Pick an integer between 1 and 100: "))
    if human_guess > computer_number:
        print("your guess is too high")
    elif computer_number > human_guess:
        print("your guess is too low")
    elif computer_number == human_guess:
        print("good for you")

