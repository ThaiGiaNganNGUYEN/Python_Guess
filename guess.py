import random

secret = random.randint(1, 101)
num_guess = 1
guess = int(input("Enter your guess: "))
while (guess != secret):
    if (guess > secret):
        print("Guess is too high! Try again.\n")
    else:
        print("Guess is too low! Try again.\n")
    num_guess += 1
    guess = int(input("Enter your guess: "))
print("That's correct! The secret number is: ", secret)
print("You got it in: ", num_guess, " guesses!\n")