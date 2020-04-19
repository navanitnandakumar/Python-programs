#game board structure
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
#global variables
game_still_going = True
winner = None
current_player = 'X'

def display_board():
    #to display board
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def handle_turn(player):
    #handles a turn
    print(player + "'s turn.")
    position = input("Choose a position from 1 to 9 -->")
    valid = False

    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Invalid input! Choose a position from 1 to 9 -->")
        position = int(position)-1
        if board[position]=='-':
            valid = True
        else:
            print("No cheating!")

    board[position] = player
    display_board()

def check_if_game_over():
    #checks if game is over
    check_if_win()
    check_if_tie()

def check_if_win():
    #calls fns, checks for win
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
    #checks rows
    global game_still_going
    row_1_win = board[0] == board[1] == board[2] != "-"
    row_2_win = board[3] == board[4] == board[5] != "-"
    row_3_win = board[6] == board[7] == board[8] != "-"

    if row_1_win or row_2_win or row_3_win:
        game_still_going = False

    if row_1_win:
        return board[0]
    elif row_2_win:
        return board[3]
    elif row_3_win:
        return board[6]
    return

def check_columns():
    #checks columns
    global game_still_going
    column_1_win = board[0] == board[3] == board[6] != "-"
    column_2_win = board[1] == board[4] == board[7] != "-"
    column_3_win = board[2] == board[5] == board[8] != "-"

    if column_1_win or column_2_win or column_3_win:
        game_still_going = False

    if column_1_win:
        return board[0]
    elif column_2_win:
        return board[1]
    elif column_3_win:
        return board[2]
    return

def check_diagonals():
    #checks diagonals
    global game_still_going
    diagonal_1_win = board[0] == board[4] == board[8] != "-"
    diagonal_2_win = board[2] == board[4] == board[6] != "-"

    if diagonal_1_win or diagonal_2_win:
        game_still_going = False

    if diagonal_1_win:
        return board[0]
    elif diagonal_2_win:
        return board[2]
    return

def check_if_tie():
    #checks for ties
    global game_still_going
    if '-' not in board:
        game_still_going = False
    return

def flip_player():
    #flips turns
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return

def play_game():
    #main function
    display_board()

    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " won!")
    elif winner == None:
        print("Its a tie!")

play_game()
