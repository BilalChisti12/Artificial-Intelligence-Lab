import math

# Board representation
board = [" " for _ in range(9)]

# Print board
def print_board():
    for i in range(3):
        print(board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("--+---+--")

# Check winner
def check_winner(b, player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],   # rows
        [0,3,6],[1,4,7],[2,5,8],   # columns
        [0,4,8],[2,4,6]            # diagonals
    ]
    
    for pos in win_positions:
        if b[pos[0]] == b[pos[1]] == b[pos[2]] == player:
            return True
    return False

# Check draw
def is_draw(b):
    return " " not in b

# Minimax algorithm
def minimax(b, depth, is_maximizing):
    
    if check_winner(b, "O"):
        return 1
    if check_winner(b, "X"):
        return -1
    if is_draw(b):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth + 1, False)
                b[i] = " "
                best_score = max(score, best_score)
        return best_score

    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth + 1, True)
                b[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            
            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"

# Game loop
def play_game():
    while True:
        print_board()

        # Player move
        move = int(input("Enter position (0-8): "))
        if board[move] != " ":
            print("Invalid move")
            continue

        board[move] = "X"

        if check_winner(board, "X"):
            print_board()
            print("You win!")
            break

        if is_draw(board):
            print_board()
            print("Draw!")
            break

        # AI move
        ai_move()

        if check_winner(board, "O"):
            print_board()
            print("AI wins!")
            break

        if is_draw(board):
            print_board()
            print("Draw!")
            break

play_game()
