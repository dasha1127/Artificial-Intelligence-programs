def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()

def is_safe(board, row, col):
    # Check the column
    for i in range(row):
        if board[i][col]:
            return False
    
    # Check the upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    
    # Check the upper right diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j]:
            return False
        i -= 1
        j += 1
    
    return True

def solve_n_queens(board, row):
    if row >= len(board):
        print_board(board)
        return True
    
    solution_found = False
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = True
            solution_found = solve_n_queens(board, row + 1) or solution_found
            board[row][col] = False
    
    return solution_found

def main():
    n = 8
    board = [[False] * n for _ in range(n)]
    solve_n_queens(board, 0)

if __name__ == "__main__":
    main()
