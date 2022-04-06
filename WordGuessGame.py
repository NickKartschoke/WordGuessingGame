from asyncore import read
from curses.ascii import isalpha
import random
from re import S

file_path = (r"C:\Users\nickk\repo\words_alpha.txt")
f = open(file_path)
lines = f.read().split('\n')
check = False
user_input1 = 'no'
while(user_input1 != 'quit'):
    guess_remaining = 7
    rand = random.randint(0,len(lines))
    wordList = list(lines[rand])
    word = lines[rand]
    guess_remaining = 7
    blankWord = list('_'*len(word))
    check = False
    while guess_remaining > 0:
        char_loaction = list()
        if '_' not in blankWord:
            print("You win! The word was: ", word)
            break
        user_input = input("Enter word or letter: ")
        user_input = user_input.lower()
        if user_input == 'quit':
            break
        if len(user_input) == 1 and user_input.isalpha():
            check = user_input in wordList
            if check == True:
                for i in range(0,len(word)):
                    if  wordList[i] == user_input:
                        blankWord[i] = user_input
                print(blankWord)
            else:
                guess_remaining -= 1
                print("Guesses remaining: ", guess_remaining)
        elif len(user_input) > 1 and user_input.isalpha():
            check = user_input == word
            if check == True:
                blankWord = list(user_input)
            else:
                guess_remaining -= 1
                print("Guesses remaining: ", guess_remaining)
        else:
            print("Incorrect character!")
    if guess_remaining == 0:
        print("You lose! The word was: ", word)
    if user_input != 'quit':
        user_input1 = input("Type quit to stop playing, or press any key to continue: ")
        user_input1.lower()
    else:
        break
f.close()
