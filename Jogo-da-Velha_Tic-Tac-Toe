#4.6.2.1 PROJETO: Tic-Tac-Toe;

from random import randrange

def displayboard(board):
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   {}   |   {}   |   {}   |'.format(board[0][0], board[0][1], board[0][2]))
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   {}   |   {}   |   {}   |'.format(board[1][0], board[1][1], board[1][2]))
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   {}   |   {}   |   {}   |'.format(board[2][0], board[2][1], board[2][2]))
    print('|       |       |       |')
    print('+-------+-------+-------+')

def enter_move(board):
    while True:
        move = int(input('Pick a number within the range of squares (1-9): '))
        if move < 1 or move > 9:
            print("It's not an number in the range of 1 through 9.")
            continue
        elif move not in board[0] and move not in board[1] and move not in board[2]:
            print("Sorry, that square is alredy taken! Please select another square!")
            continue
        for row in range(0,3):
            for column in range(0,3):
                if board[row][column] == int(move):
                    board[row][column] = 'O'
        break

def listfreefields(board):
    global fre_boardlist
    fre_boardlist= []
    for row in range(0, 3):
        for column in range(0, 3):
            if board[row][column] == 'X' or board[row][column] == 'O':
                pass
            else:
                fre_boardlist.append(([row], [column]))
                continue
    print(fre_boardlist)

def victory_for(board, sign):
        if sign == 'O':
            print('Checking to see if YOU are the winner!')
        else:
            print('Checking to see if the computer has won the game')
        if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
            return True
        elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
            return True
        elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
            return True
        elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
            return True
        elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
            return True
        elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
            return True
        elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
            return True
        elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
            return True
        else:
            print('We DO NOT have a winner!')

def draw_move(board):
    while True:
        row = randrange(3)
        column = randrange(3)
        if ([row], [column]) not in fre_boardlist:
            continue
        else:
            board[row][column] = 'X'
            return

player = 'O'
computer = 'X'
num_plays = 1
board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

## Início do jogo (start of the game):

print('WELCOME TO THE GAME!\n\nThere is the actual status of the game!\n\nThe computer starts:\n')
displayboard(board)

while num_plays < 9:

## O código abaixo é referente ao turno do jogador(Player turn):

    enter_move(board)
    num_plays += 1
    displayboard(board)
    if num_plays >= 6:
        if victory_for(board, player) == True:
            print("Congratulations! You win!")
            break
        else:
            continue
    else:
        print('Here is the current list of free squares and the status: ')
        listfreefields(board)
        print()
        displayboard(board)

## O código abaixo é referente ao turno do computador:

    print('\nNow is the computer turn!\n')
    draw_move(board)
    num_plays += 1
    displayboard(board)
    if num_plays >= 5:
        if victory_for(board, computer) == True:
            print("The computer Wins!")
            break
        else:
            continue
    else:
        print('Here is the current list of free squares and the status: ')
        listfreefields(board)
        print()
        displayboard(board)
else:
    print("This is a 'cat's game'!")
print('\nThank you for playing!! Please play again soon!')
