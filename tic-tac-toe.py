import math

HUMAN = 'O'    
AI = 'X'       

def moveLeft(board):
    for row in board:
        for i in row:
            if i == '_':
                return True
    return False

def evaluateBoard(board):
    for i in range(3):
        # row
        if board[i][0] == board[i][1] == board[i][2] != '_':
            if board[i][0] == AI:
                return +10
            elif board[i][0] == HUMAN:
                return -10
        # column
        if board[0][i] == board[1][i] == board[2][i] != '_':
            if board[0][i] == AI:
                return +10
            elif board[0][i] == HUMAN:
                return -10
    # diagonal
    if board[0][0] == board[1][1] == board[2][2] != '_':
        if board[0][0] == AI:
            return +10
        elif board[0][0] == HUMAN:
            return -10
    if board[0][2] == board[1][1] == board[2][0] != '_':
        if board[0][2] == AI:
            return +10
        elif board[0][2] == HUMAN:
            return -10
    #no one won
    return 0

def minimax(board, is_maximizing):
    score = evaluateBoard(board)
    if score == 10 or score == -10:
        return score
    if not moveLeft(board):
        return 0
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = AI
                    best_score = max(best_score, minimax(board, False))
                    board[i][j] = '_'
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = HUMAN
                    best_score = min(best_score, minimax(board, True))
                    board[i][j] = '_'
        return best_score

def find_best_move(board):
    #find best move for AI
    best_value = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = AI
                move_value = minimax(board, False)
                board[i][j] = '_'
                if move_value > best_value:
                    best_move = (i, j)
                    best_value = move_value
    return best_move

def print_board(board):
    print("\nCurrent Board : ")
    for row in board:
        for i in row:
            print(i , end= " ")
        print()
    print()

def is_valid_move(board, x, y):
    if 0 <= x <=2  and 0 <= y <= 2 and board[x][y] == '_':
        return True 
    return False

def game_over(board):
    if evaluateBoard(borad) != 0 or not moveLeft(board):
        return True
    return False

def main():
    board = [['_', '_', '_'],
             ['_', '_', '_'],
             ['_', '_', '_']]
    print("welcome to Tic-Tac-Toe written by Aras Valizadeh :).")
    print("you are 'O' ,AI is 'X'.")
    print("enter your move as 'row col' (without quotes) , where row and col are numbers from 1 to 3.")
    print_board(board)
    while True:
        #human turn
        while True:
            move = input(" Your move (row col): ").split()
            if len(move) != 2:
                print(" Please enter two numbers separated by a space.")
                continue
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if not is_valid_move(board, x, y):
                print("Invalid move. Try again.")
                continue
            board[x][y] = HUMAN
            break
        
        print_board(board)
        if game_over(board):
            break

        #AI turn
        print("AI is making a move...")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = AI

        print_board(board)
        if game_over(board):
            break
        
    score = evaluateBoard(board)
    if score == 10:
        print("AI wins!")
    elif score == -10:
        print("You win!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()