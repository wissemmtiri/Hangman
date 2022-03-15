# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 16:54:35 2022

@author: Wissem
"""

from wordlist import words
from hangman import logo,stages
import random

def hangman():
    #--------------STARTING--------------
    lives = len(stages)-1
    
    print(logo)
    print(stages[0])
    
    #--------------CHOOSING_THE_WORD--------------
    chosen_word = words[random.randrange(1,len(words))]
    #print(chosen_word)
    
    #--------------LIST TO FILL-------------- 
    to_fill = []
    for i in chosen_word:
        to_fill += '_'
    mistake = []
        
    #--------------FILLING PROCESS--------------    
    end_of_game = False
    while(not end_of_game):
        while(True):
            choice = input("GIVE A TRY : ").lower()
            if (len(choice) != 1):
                print("PLEASE ENTER A SINGLE CARACTER : ")
            else : 
                break
        if choice in chosen_word :
            for i in range(len(chosen_word)):
                if choice == chosen_word[i] :
                    if choice not in to_fill:
                        to_fill[i] = choice
                        print(''.join(to_fill))
                    else:
                        print("YOU ALREADY GUESSED THIS ONE. Try again")
            if (''.join(to_fill) == chosen_word):
                print("YOU GUESSED IT RIGHT,")
                end_of_game = True
        else :
            if choice in mistake:
                print("YOU ALREADY TRIED THIS AND IT IS WRONG.")
            else :
                mistake += choice
                print(stages[len(stages)-lives])
                lives -= 1
                print("YOU STILL HAVE ",lives," LIVES")
                print(''.join(to_fill))
                if(lives == 1):
                    print(stages[len(stages)-lives])
                    print("YOU LOST.")
                    end_of_game = True
    print("THE WORD IS : ",chosen_word)  
    input()   

hangman()