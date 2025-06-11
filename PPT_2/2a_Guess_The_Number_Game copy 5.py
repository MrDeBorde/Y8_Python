
#2a_Guess_the_Number_Game.py

''' 🎮 1. "Guess the Number" Game.py
Concepts: if/elif/else, comparison operators, input, random
Task:
Create a simple number guessing game where:

The program randomly selects a number between 1 and 20.

The user guesses the number.

The program tells the user if the guess is too high, too low, or correct.

🔧 Extension: Add a score counter for number of attempts. '''

import random

secret = random.randint(1, 20)   # computer picks a number
guess = int(input("I'm thinking of a number between 1 and 20. Guess: "))

while guess != secret:
    if guess < secret:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Try again: "))

print("You got it! The number was", secret)
