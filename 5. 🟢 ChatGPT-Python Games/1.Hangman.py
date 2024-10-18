
"""
How it works:
Word Selection: The program randomly selects a word from word_list.
Displaying Progress: It displays the word with blanks (_) for unguessed letters.
User Input: The user guesses letters, and the program checks if the letter is in the word.
Tracking Attempts: The player gets 6 wrong guesses before losing.
Win/Loss Conditions: The game ends when the word is fully guessed or when attempts run out.
"""


import random

# List of words to choose from
word_list = ['python', 'java', 'hangman', 'programming', 'developer']

# Randomly select a word
word = random.choice(word_list)
guessed_letters = []
attempts = 6

# Function to display the current progress of the word
def display_word():
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

# Game loop
while attempts > 0:
    print(f"\nWord: {display_word()}")
    guess = input("Guess a letter: ").lower()

    # Check if the guess is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please guess a single letter.")
        continue

    # If the guessed letter is already guessed
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try again.")
        continue

    guessed_letters.append(guess)

    # Check if the guessed letter is in the word
    if guess in word:
        print(f"Good job! '{guess}' is in the word.")
    else:
        attempts -= 1
        print(f"Wrong guess! '{guess}' is not in the word. Attempts left: {attempts}")

    # Check if the word is fully guessed
    if set(word) <= set(guessed_letters):
        print(f"\nCongratulations! You guessed the word: {word}")
        break
else:
    print(f"\nYou lost! The word was '{word}'. Better luck next time.")
