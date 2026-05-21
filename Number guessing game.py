# Number Guessing Game

import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0

print("Welcome to the Number Guessing Game!")

while True:
    # Get user input
    guess = int(input("Guess a number between 1 and 100: "))

    attempts += 1

    # Check the guess
    if guess < secret_number:
        print("Too low!")

    elif guess > secret_number:
        print("Too high!")

    else:
        print(f"Correct! You guessed the number in {attempts} attempts.")
        break