"""
How it works:
Game Board: The game board is represented as a list of 9 spaces.
Printing the Board: The print_board() function displays the current state of the board.
Winning Conditions: The check_winner() function checks for winning conditions after each move.
Game Loop: Players take turns entering their moves:
Input is validated to ensure it's within range and the chosen cell is empty.
The board is updated, and the program checks for a winner after each move.
End Conditions: The game ends when a player wins or all spaces are filled (resulting in a tie).
"""

# Initialize the game board
board = [' ' for _ in range(9)]


# Function to print the current board
def print_board():
    print("\n")
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i + 1]} | {board[i + 2]}")
        if i < 6:
            print("---------")
    print("\n")


# Function to check for a winner
def check_winner(player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
        (0, 4, 8), (2, 4, 6)  # diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


# Main game loop
current_player = 'X'
for turn in range(9):
    print_board()

    # Get user input
    move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

    # Validate the input
    if move < 0 or move >= 9 or board[move] != ' ':
        print("Invalid move, try again.")
        continue

    # Make the move
    board[move] = current_player

    # Check for a winner
    if check_winner(current_player):
        print_board()
        print(f"Player {current_player} wins!")
        break

    # Switch player
    current_player = 'O' if current_player == 'X' else 'X'
else:
    print_board()
    print("It's a tie!")
