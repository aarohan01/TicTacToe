#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint 


# In[2]:


def display(board) :
    
    ''' This function displays the board. '''
    
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print(f'---|---|---')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print(f'---|---|---')
    print(f' {board[7]} | {board[8]} | {board[9]} ')


# In[3]:


def board_help() :
    
    ''' This function is to inform users about the gameplay. '''
    
    print('How to play : \n')
    print('Game will be played betwwen two players.')
    print('Board is 3 X 3 grid. Each spot is numbered as follows : \n')
    display(['#',1,2,3,4,5,6,7,8,9])
    print('\n')
    print('Each player will get a chance to mark the board with X or O , by entering the spot number. ')
    print('Player with three consecutive marks [ X or O ] wins !!!')
    print('\n\n')


# In[4]:


def clear() :
    ''' This function is to clear the screen. '''
    print('\n\n'*100)


# In[5]:


def players() :
    
    ''' This function is to store user names and marks. '''
    marks = ['X','O']
    
    ### Clear screen ###
    clear()   
    
    ### Intro ###
    print('Player 1 : Enter name') 
    p1_name = str(input())
    p1_mark = str()
    while p1_mark not in marks :
            print(f'Hi {p1_name} ! Please select your mark [X/O] : ')
            p1_mark = str(input()).upper()
    
    marks.remove(p1_mark)
    
    
    print('Player 2 : Enter name') 
    p2_name = str(input())
    p2_mark = marks[0]
    clear()
    
    ### Print info ###
    print(f'{p1_name} : {p1_mark} ')
    print(f'{p2_name} : {p2_mark} ')
    
    return (p1_name,p2_name,p1_mark,p2_mark)
    


# In[6]:


def wincheck(gboard,mark) :
    
    ''' This function is to check winning condition. '''

    patterns = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    
    for pattern in patterns :
        if gboard[pattern[0]] == gboard[pattern[1]] == gboard[pattern[2]] == mark :
            return True
        
    
    return False  # If no matches 
    


# In[7]:


def who_plays() :
    
    who = randint(1,2)
    return who 
    


# In[8]:


def game() :
    
    ''' This function is the gameplay. '''
    
    ### Players info ###
    p1n,p2n,p1m,p2m = players()
    
    ### Player flag : which player is playing ### odd number player 1 , even number player 2 ###
    pflag = who_plays()
    if pflag == 1 :
        print(f'Player {p1n} plays first !')
    else :
        print(f'Player {p2n} plays first !')
    
    ### Board ###
    gboard = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
    ### Game ###
    def play(name,mark) :
        print(f'{name}\'s chance : Enter grid number to mark {mark} [0-9] : ')
        
        ### Out of bounds check ###
        grid_int = int(input())
        while  grid_int > 9 or grid_int < 1:
                print('\n')
                print(f'Enter a number between 0-9 only !')
                print(f'{name}\'s chance : Enter grid number to mark {mark} [0-9] : ') 
                grid_int = int(input())
        
        ### Check if mark already exists ###
        while gboard[grid_int] != ' ' :
                print('\n')
                print(f'Mark {gboard[grid_int]} is already present at this grid number !! ')
                print(f'{name}\'s chance : Enter another grid number to mark {mark} : ')
                grid_int = int(input())
                      
        ### Set board ###              
        gboard[grid_int] = mark
        clear()
        #print(gboard)   #prints the gboard array to debug 
        display(gboard)
        if wincheck(gboard,mark) :
            print('\n')
            print(f'Player {name} wins !!! Congratulations !!!')
            return True
        
    
    
    while True :
            
            if pflag == 10 :
                print('Nobody won !!!')
                break      
            elif pflag%2 != 0 :
                if play(p1n,p1m) :
                    break
                pflag += 1
            else :
                if play(p2n,p2m) :
                    break
                pflag += 1
                
    #Game over
                
            
           


# In[9]:


def main() :
    
    ''' This is the main function. This will control everything. '''
    
    ### Welcome ###
    print('Welcome to Tic Tac Toe. ')
    print('\n')
    board_help()
    
    ### Start ###
    print('Are you ready to play the game ? : [Y/N] ')
    start = str(input()).upper()
    
    while True :
        if start not in {'N','NO','Y','YES'} :
            print('Wrong Input. Enter either Y or N : ')
            start = str(input())
            continue
        elif start in {'N','NO'} :
            print('Bye. Have a nice day !!!')
            break
        else : 
            game()
            print('Want to replay ? : [Y/N] ')
            start = str(input())
            
    
        


# In[ ]:


main()


# In[ ]:





# In[ ]:




