def displayboard(board):
    
    print(board[7]+ ' | ' +board[8]+ ' | ' +board[9])
    print('--|---|--')
    print(board[4]+ ' | ' +board[5]+ ' | ' +board[6])
    print('--|---|--')
    print(board[1]+ ' | ' +board[2]+ ' | ' +board[3])
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
displayboard(board)

def playerinput():
    m = ''
    while m!='X'  and m!='O':
        m = input(" Player 1 - Choose X or Y :- ")
    
    if m == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, m, position):
    board[position] = m
def win_check(board, m):
    return ((board[7] == m and board[8] == m and board[9] == m) or
            (board[4] == m and board[5] == m and board[6] == m) or
            (board[1] == m and board[2] == m and board[3] == m) or
            (board[7] == m and board[4] == m and board[1] == m) or
            (board[8] == m and board[5] == m and board[2] == m) or
            (board[9] == m and board[6] == m and board[3] == m) or
            (board[7] == m and board[5] == m and board[3] == m) or
            (board[9] == m and board[5] == m and board[1] == m ))
import random
def choose_first():
    if random.randint(0,1)==0:
        return 'Player 2'
    else:
        return 'Player 1'
def space_check(board, position):
    return board[position]== ' '
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input(' -> Choose your next position: (1-9) '))
    return position
def replay():
    return input(' -> Do you want to play it again? Enter Y/N ')

#----------- The Main Code Goes From Here-------

print(' ---------- Welcome To Tic Tac Toe! Game ----------')
print('----------------------------------------------------')

while True:
    theBoard = [' ']*10
    player1_m, player2_m = playerinput()
    turn = choose_first()
    print(turn + ' will go first to Start!')
    play_game = input(' -> Are You Guys Ready To Play? Enter Y/N ')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1' :
            displayboard(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_m, position)
            if win_check(theBoard, player1_m):
                displayboard(theBoard)
                print('Congratulations! Player 1 You WON!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    displayboard(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            displayboard(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_m, position)

            if win_check(theBoard, player2_m):
                displayboard(theBoard)
                print('Congratulations! Player 2 You WON!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    displayboard(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
            
        
