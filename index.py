import numpy as np
from colorama import init, Fore, Style

color1="X"
color2="O"
player1=1
player2=2

def validate_int_number():
    possible_number= input('Write a character:')
    try:
        number=int(possible_number)
        print("This is an integer")
    except ValueError:
        print("This isn't an integer")

def create_board(nRows,nColumns):
    board= np.zeros((nRows,nColumns),str)
    
    for nrow in range(nRows):
        for ncol in range(nColumns):
            board[nrow][ncol]=''
    return (board)
    
def print_board(board):
    #HEAD
    print('|', end='')
    for element in range(1,len(board[0])+1):
        print(element,end='|')
    print("")
    #TABLE
    for nrow in board:
        print("|",end=' ')        
        for value in nrow:
            print("|", end=' ')
            player_color= Fore.CYAN
            if value==color2:
                player_color= Fore.MAGENTA
            print(player_color + value,end='')
            print(Style.RESET_ALL,end='')
        print('')
    #FOOT
    for element in range(len(board[0])):
        print("+",end="-")
    print('+')


def get_valid_row_in_column(column,board):
    index= len(board)-1
    output=-1
    while index>=0:
        if board[index][column] == ' ':
            output= index
        index-=1
    return output

def request_column(board):
    while True:
        column= validate_int_number("Enter the column to place the piece:")
        if column <= 1 or column > len(board[0]):
            print('The number column is invalid')
        
        elif board[0][column-1]!= ' ':
            print('The column is full')
        
        else:
            column-1


def Enter_piece(column,player,board):
    color=color1
    if player==player2:
        color=color2
    row= get_valid_row_in_column(column,board)
    assignament=True
    if row==-1:
        assignament=False
    board[row][column]=color
    return assignament
    



tab= create_board(7,6)
tab2= print_board(tab)


