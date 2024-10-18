"""
How it works:
Random Number: The computer generates a random number between 1 and 100 using random.randint().
User Input: The player guesses the number by entering their guess.
Feedback: The program tells the player if their guess is too low, too high, or correct.
Win Condition: The game ends when the player guesses the correct number.
"""
import random

# Computer picks a random number between 1 and 100
number = random.randint(1, 100)

# Initialize guess variable
guess = None

# Game loop until the user guesses the correct number
while guess != number:
    # Get the user's guess
    guess = int(input("Guess a number between 1 and 100: "))

    # Provide feedback if the guess is too high, too low, or correct
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number {number} correctly!")
