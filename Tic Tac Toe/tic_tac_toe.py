import random

# Define the Tic-Tac-Toe board
board = [' ' for _ in range(9)]

# Define winning combinations
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if the board is full
def is_board_full(board):
    return ' ' not in board

# Function to check if a player has won
def check_win(board, player):
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to evaluate the current state of the board
def evaluate(board):
    if check_win(board, 'X'):
        return 1
    elif check_win(board, 'O'):
        return -1
    else:
        return 0

# Minimax function with Alpha-Beta Pruning
def minimax(board, depth, maximizing_player, alpha, beta):
    if check_win(board, 'X'):
        return 1
    elif check_win(board, 'O'):
        return -1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Function to find the best move for the AI
def best_move(board):
    best_eval = float('-inf')
    best_move = -1
    alpha = float('-inf')
    beta = float('inf')

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            eval = minimax(board, 0, False, alpha, beta)
            board[i] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move

# Main game loop
while True:
    print_board(board)
    player_move = int(input("Enter your move (0-8): "))

    if board[player_move] == ' ':
        board[player_move] = 'O'

        if check_win(board, 'O'):
            print_board(board)
            print("You win!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        ai_move = best_move(board)
        board[ai_move] = 'X'

        if check_win(board, 'X'):
            print_board(board)
            print("AI wins!")
            break
    else:
        print("That space is already taken. Try again.")
