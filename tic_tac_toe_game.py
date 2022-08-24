#!/usr/bin/env python
# coding: utf-8

# In[2]:


def display(mylist):
    print("|"+mylist[7]+"|"+mylist[8]+"|"+mylist[9]+"|")
    print("|"+mylist[4]+"|"+mylist[5]+"|"+mylist[6]+"|")
    print("|"+mylist[1]+"|"+mylist[2]+"|"+mylist[3]+"|")


# In[3]:


from IPython.display import clear_output


# In[4]:


def user_input(entered_value_list,player):
    check_move= False
    #entered_value_list=[]
    while check_move == False:
        
        input_num=input(f"{player} Please enter the number between 1 to 9: ")
        if input_num.isdigit():
            if int(input_num) in range(1,10):
                print(f"You have entered the correct choice .. {player}")
                if int(input_num) not in entered_value_list:
                    print(f"You have entered the correct choice .. {player}")
                    entered_value_list.append(int(input_num))
                    check_move = True
                    return int(input_num)
                else:
                    print("Value already entered, please enter a new index")
                    
                
            else:
                print(f" {player}, Please enter the value with in range from 1 to 9")
        else :
            print(f"{player}, Please enter the integer value between 1 and 9")
    #clear_output()
    return int(input_num)


# In[5]:


def list_update(mylist,position):
    
    #value to be insert
    check_input=False
    while check_input == False:
        new_value = input("Please insert the value in  X or 0 ")
        if new_value not in ('X','0'):
            print("Please enter the value in X or 0")
        else:
            print("Procedding with your input")
            check_input = True
    
    
    mylist[position] = new_value


# In[6]:


def game_choice():
    user_choice= False
    
    while user_choice not in ('Y','N'):
        user_choice =input("keep playing ? (Y/N)")
        
    if user_choice == 'Y':
        return True
    else :
        return False    


# In[7]:


def check_win(my_list,player):
    player_dictionary= {'Player1':'X','Player2':'0'}
    
    if (my_list[1] == player_dictionary[player] and my_list[2] == player_dictionary[player] and my_list[3] == player_dictionary[player]) or        (my_list[1] == player_dictionary[player] and my_list[4] == player_dictionary[player] and my_list[7] == player_dictionary[player]) or        (my_list[1] == player_dictionary[player] and my_list[5] == player_dictionary[player] and my_list[9] == player_dictionary[player]) or        (my_list[2] == player_dictionary[player] and my_list[5] == player_dictionary[player] and my_list[8] == player_dictionary[player]) or        (my_list[3] == player_dictionary[player] and my_list[6] == player_dictionary[player] and my_list[9] == player_dictionary[player]) or        (my_list[3] == player_dictionary[player] and my_list[5] == player_dictionary[player] and my_list[7] == player_dictionary[player]) or        (my_list[4] == player_dictionary[player] and my_list[5] == player_dictionary[player] and my_list[6] == player_dictionary[player]) or        (my_list[7] == player_dictionary[player] and my_list[8] == player_dictionary[player] and my_list[9] == player_dictionary[player]):
            print(f"Congratulations !!! {player} you have won")
            return True
        
    else:
        return False


# In[8]:


def play_game():
    my_list=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player=''
    entered_value_list=[]
    game_on =True
    check_won = False
    while game_on:
        display(my_list)
    
        for i in range(1,10):
            if i % 2 == 0:
                player ='Player2'
            else:
                player ='Player1'
            player_choice=user_input(entered_value_list,player)
        
            list_update(my_list,player_choice)
            clear_output()
            display(my_list)
            check_won= check_win(my_list,player)
            if check_won:
                print("Congrats")
                break
            else:
                pass
        game_on = game_choice()


# In[9]:


play_game()


# In[ ]:





# In[ ]:




