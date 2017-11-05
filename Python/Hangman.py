# -*- coding: utf-8 -*-
"""
Created on Sun May  7 17:07:15 2017

@author: Ivan
"""
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...)")
    # inFile: file
    
    inFile = open('words.txt', 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

word = choose_word(wordlist)
def hangman(word):
    string_alpha = "abcdefghijklmnopqrstuvwxyz"
    print ("Welcome to the game, Hangman!\nI am thinking of a word that is",len(word),"words long.")
    
    list3 = []
    n = 8
    while n>0: 
        print ("You have",n,"guesses left." )
        print ("Available letters: "+ string_alpha)
        user_input = (input("Please guess a letter:"))
                       
        string_alpha = string_alpha.replace(user_input,"")
        list1 = []
        list2 = []
       
        list3.append(user_input)
               
        for i in word:
            list1.append(i)
        
        for j in list1:
            if j in list3:
                list2.append(j)
            else:
                list2.append("_")
        
        
        if user_input in list1:
            print ("Good guess:")
            print (list2)
            if list1 in list3:
                print("Congratulations, you won!")
                return 0
        else:
            print ("Oops! That letter is not in my word:")
            print (list2)
            n-=1
        
    print('I am sorry. you lost. Do you want to play again?')
    ans =input("Do you want to play again? Y/N")
    if ans == "y":
        word = choose_word(wordlist)
        hangman(word)
    else:
        None