"""
How it works:
Choices: Both the user and the computer choose between 'rock', 'paper', or 'scissors'.
Random Computer Choice: The computer randomly selects one of the three options.
User Input: The user enters their choice, and the program validates the input.
Winning Logic: The game compares the user’s and computer’s choices to determine the winner:
Rock beats Scissors
Scissors beats Paper
Paper beats Rock
Exit Condition: The user can type "quit" to stop playing.
"""
import random

# List of possible choices
choices = ['rock', 'paper', 'scissors']

# Game loop
while True:
    # Computer randomly selects Rock, Paper, or Scissors
    computer_choice = random.choice(choices)

    # User input
    user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop playing): ").lower()

    # Exit the game if the user types 'quit'
    if user_choice == 'quit':
        print("Thanks for playing!")
        break

    # Check for valid input
    if user_choice not in choices:
        print("Invalid choice, please try again.")
        continue

    # Display choices
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
    else:
        print("You lose!")
