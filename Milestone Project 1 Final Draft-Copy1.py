#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output

gameboard = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
gameboard_example = ['#','1','2','3','4','5','6','7','8','9']

def display_board(board):
    
    row1 = [board[7],board[8],board[9]]
    row2 = [board[4],board[5],board[6]]
    row3 = [board[1],board[2],board[3]]
    
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print('---------')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print('---------')
    print(f'{board[1]} | {board[2]} | {board[3]}')
    


# In[2]:


def player_input():
    
    p1 = 'Mario'
    p2 = 'Luigi'
    
    while p1 not in ['X','x','O','o']:
        
        p1 = input('Player 1, Please choose your character (X or O): ')
        
        if p1 not in ['X','x','O','o']:
            
            print()
            print(f'Sorry, {p1} is not available')
            
    if p1.upper() == 'X':
        p2 = 'O'
    else:
        p2 = 'X'
    return p1

            
            


# In[3]:


def place_marker(board, marker, postion):
    board.pop(position)
    board.insert(position,marker)


# In[4]:


def win_check(board,mark):
    
    
    s1 = [board[1],board[2],board[3]]
    s2 = [board[4],board[5],board[6]]
    s3 = [board[7],board[8],board[9]]
    s4 = [board[7],board[4],board[1]]
    s5 = [board[8],board[5],board[2]]
    s6 = [board[9],board[6],board[3]]
    s7 = [board[1],board[5],board[9]]
    s8 = [board[7],board[5],board[3]]
    
    possible_solutions = [s1,s2,s3,s4,s5,s6,s7,s8]
    
    win_condition = [mark,mark,mark]
    
    while win_condition in possible_solutions:
        return True
    else:
        return False


# In[5]:


import random

def coin_toss():
    
    coin = random.randint(0,1)
    
    if coin == int(1):
        coin = 'Heads'
    else:
        coin = 'Tails'
    return coin
    


# In[6]:


def space_check(board,position):

    while board[position] == ' ':
        return True
    else:
        return False


# In[7]:


def full_board_check(board):
    
    temp = []
    
    for pos in board:
        temp.append(pos)
    if ' ' not in temp:
        return True
    else:
        return False


# In[8]:


def player_choice(board):

    choice = 'wrong'
    within_range = False
    acceptable = False
    
    while choice.isdigit() == False or within_range == False or acceptable == False:
        
        choice = input('Please enter a location(1-9): ')
        
        if choice.isdigit() == False:
            print()
            print(f'Sorry {choice} is not a digit')

        if choice.isdigit() == True:
            if int(choice) in range(1,10):
                within_range = True
                
                if space_check(board,int(choice)) == True:
                    acceptable = True
            
                else:
                    print()
                    print(f'Sorry, {choice} is already taken')    
                    acceptable = False
                
            else:
                print()
                print(f'Sorry {choice} is not a number 1-9')
                within_range = False
                
    return int(choice)
        


# In[9]:


def replay():
    
    choice = 'wrong'
    answers = ['Y','y','N','n']
    while choice not in answers:
        choice = input('Do you want to play again?(Y or N): ')
        if choice not in answers:
            print()
            print('Sorry, please choose Y or N')
            
        if choice == 'Y' or choice == 'y':
            return True
        if choice == 'N' or choice == 'n':
            return False


# In[10]:


def ready_check():
    
    ready = False
    answers = ['Y','y','N','n']
    
    while ready == False:
        choice = input('Are you ready to begin? Y or N')
        
        if choice not in answers:
            print()
            print(f'{choice} is unavailable')
        if choice in answers:
            if choice == 'Y' or choice == 'y':
                ready = True
            else:
                print()
                print('Type Y when ready')
                
    return True


# #####################################################

# In[11]:


print('Welcome to Tic Tac Toe')
print()

while ready_check() == True:
    
    game_on = False
    
    clear_output()
    
    print('These are the locations on the board')
    print()
    display_board(gameboard_example)

    print()
    
    print('This is the blank board')
    print()
    display_board(gameboard)
    
    p1 = player_input().upper()
    
    if p1 == 'X':
        p2 = 'O'
    else:
        p2 = 'X'

    
        
    game_on = True
    
    
    while game_on == True:
        
        
            clear_output()
            print('Example Board')
            print()
            display_board(gameboard_example)
            print()
            print('Current Board')
            print()
            display_board(gameboard)
            print()
            print(f'{p1} move')

            position = player_choice(gameboard)
            place_marker(gameboard,p1,position)
            
            if win_check(gameboard,p1)==True:
                clear_output()
                display_board(gameboard)
                print()
                print(f'{p1} wins!')
                break

            if full_board_check(gameboard) == True:
                clear_output()
                display_board(gameboard)
                break
                
                

            clear_output()
            print('Example Board')
            print()
            display_board(gameboard_example)
            print()
            print('Current Board')
            print()
            display_board(gameboard)
            print()
            print(f'{p2} move')

            position = player_choice(gameboard)
            place_marker(gameboard,p2,position)
            
            if win_check(gameboard,p2)==True:
                clear_output()
                display_board(gameboard)
                print()
                print(f'{p2} wins!')
                break            
            

            if full_board_check(gameboard) == True:
                clear_output()
                display_board(gameboard)
                break

                pass
    
    
    
    if not replay():
        clear_output()
        print('Thanks for playing')
        break
    
    


# In[ ]:




