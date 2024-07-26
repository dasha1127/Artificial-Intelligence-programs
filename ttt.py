def print_board(board):
    """Print the current board state."""
    print("---------")
    for row in board:
        print(f"| {' '.join(row)} |")
    print("---------")


def check_winner(board, player):
    """Check if the given player has won the game."""
    win_conditions = [
        # Horizontal
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Vertical
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    
    return [player, player, player] in win_conditions


def is_board_full(board):
    """Check if the board is full (no empty spaces)."""
    return all(cell != ' ' for row in board for cell in row)


def play_game():
    """Main function to play Tic-Tac-Toe."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    print("Tic-Tac-Toe Game!")
    print_board(board)

    while True:
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))
            
            if not (0 <= row < 3 and 0 <= col < 3):
                print("Invalid input. Row and column must be between 0 and 2.")
                continue
            
            if board[row][col] != ' ':
                print("Cell already taken. Choose another cell.")
                continue
            
            board[row][col] = current_player
            print_board(board)
            
            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break
            
            if is_board_full(board):
                print("The game is a draw!")
                break
            
            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'
        
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    play_game()
