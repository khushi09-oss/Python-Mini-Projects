def create_board():
    #return a list of 9 elements representing the tic-tac-toe board
    return [' ' for _ in range(9)]

def display_board(board):
    #display the tic-tac-toe board
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]               # diagonals
    ]
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False

def check_draw(board):
    # Check if the board is full and there is no winner
    return all(space != ' ' for space in board)

def tic_tac_toe():
    board = create_board()
    current_player = 'X'
    
    while True:
        display_board(board)
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
        
        if board[move] == ' ':
            board[move] = current_player
            
            if check_win(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                break
            elif check_draw(board):
                display_board(board)
                print("It's a draw!")
                break
            
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    tic_tac_toe()