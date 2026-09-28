import random

def print_board(board):
    """Displays the game board grid using standard index lookups."""
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")
    print("\n")

def check_winner(board, player):
    """Checks if a player has won the game."""
    # List of all 8 rows, columns, and diagonals
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)              # Diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == player and board[condition[1]] == player and board[condition[2]] == player:
            return True
    return False

def is_board_full(board):
    """Returns True if there are no empty numbered spots left."""
    for space in board:
        if space != "X" and space != "O":
            return False
    return True

def play_game():
    print("=== Human vs Computer Tic-Tac-Toe ===")
    
    # 1. Initialize a clean board numbered 1 to 9
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # ==========================================================
    # CUSTOM INITIAL SITUATION SECTION (UNCOMMENT TO USE)
    # Change the index numbers (0-8) below to set up a custom layout.
    # Reminders: index 0 is position 1, index 1 is position 2... index 8 is position 9.
    # ==========================================================
    board[0] = "O"
    board[2] = "X"
    board[3] = "X"
    board[6] = "X"
    board[7] = "O"
    board[8] = "O"
    # ==========================================================

    # 2. Pick Symbols
    while True:
        p1 = input("Choose your symbol (X or O): ").strip().upper()
        if p1 == "X" or p1 == "O":
            break
        print("Invalid choice. Type X or O.")
        
    if p1 == "X":
        p2 = "O"
    else:
        p2 = "X"
        
    print(f"\nSetup complete: You are '{p1}' and Computer is '{p2}'.")
    
    # 3. Choose who goes first
    # If using a custom layout, change this manually if you want the computer to start first.
    current_player = "X" 

    # 4. Main Gameplay Loop
    while True:
        print_board(board)

        # Check win/draw states before the turn
        if check_winner(board, p1):
            print("Congratulations! You won! 🎉")
            print("Name:Shashwat Parajuli")
            break
        if check_winner(board, p2):
            print("Game Over! The computer won. 🤖")
            print("Name:Shashwat Parajuli")
            break
        if is_board_full(board):
            print("It's a draw! 🤝")
            print("Name:Shashwat Parajuli")
            break

        # Move execution
        if current_player == p1:
            # Human's Turn
            try:
                move = int(input(f"Your turn ({p1}). Choose an empty spot (1-9): ")) - 1
            except ValueError:
                print("Please type a valid number.")
                continue
        else:
            # Computer's Turn
            print("Computer is moving...")
            available = [i for i in range(9) if board[i] != "X" and board[i] != "O"]
            move = random.choice(available)
            print(f"Computer picked spot {move + 1}")

        # Process the chosen move if it is valid
        if move >= 0 and move <= 8 and board[move] != "X" and board[move] != "O":
            board[move] = current_player
            
            # Switch current player rotation sequence
            if current_player == p1:
                current_player = p2
            else:
                current_player = p1
        else:
            print("That position is invalid or already filled. Try again.")

if __name__ == "__main__":
    play_game()
