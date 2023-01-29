import random
import linecache
import os
import time
from wisielec_print import wisielec
import pathlib

path = pathlib.Path('./')

def graj():
    global word
    global lives
    count = 0
    guessed_letters = []
    selected_so_far = []
    lives = 7 # ilość żyć
    clear()
    print("Please choose the dictionary:")
    print("(1) Polish or (2) English.")

    while True:
        letter_lang_choice = input("..:")
        if letter_lang_choice == "1":
            lineno = random.randint(1, 258995)  # ilość słów    
            word = (linecache.getline("slowa.txt", lineno)).strip().rstrip("/n").upper()
            break
        elif letter_lang_choice == "2":
            lineno = random.randint(1, 58110)  # ilość słów    
            word = (linecache.getline("words.txt", lineno)).strip().rstrip("/n").upper()
            break
        else:
            pass

    letters = set(word)
    zgaduj(letters, count, guessed_letters, selected_so_far)

def clear():
    time.sleep(2)
    os.system('clear')
    time.sleep(0.5)
    print(" +++++++++++++++++")
    print(" + H A N G M A N +")
    print(" +++++++++++++++++")
    print()

def zgaduj(letters, count, guessed_letters, selected_so_far):  
    clear()
    print(wisielec[count])
    print()
    print(rysuj(guessed_letters))
    print()
    if lives-count > 1:
        print(f"You have {lives-count} lives, the gallows is waiting.")
    else:
        print("The Last Chance!")
    print()

    x = (input("Guess the letter: ")).upper()
    if x in letters:
        print("YOU GUESSED!!")
        letters.remove(x)
        guessed_letters.append(x)
    elif x in selected_so_far:
        print("You have already chosen that letter, please try again.\n")
        selected_so_far.sort()
        selected_so_far_str = ", ".join(selected_so_far)
        print(f"The letters you have tried so far: {selected_so_far_str} \n")
        input("Press any key.")
        zgaduj(letters, count, guessed_letters, selected_so_far)
    else:
        count = count + 1
        print("NOT GUESSED!!")
        if count == lives:
            clear()
            print(wisielec[count])
            print(f"Game over... word: {word}")
            exit()        
    
    if len(letters) == 0:
        clear()
        print("CONGRATULATIONS!!!!")
        print(wisielec[8])
        count = 0
        guessed_letters = []
        selected_so_far=[]
        czy = (input("Do you want to play again? (y/n): ")).lower()
        if czy == 'y':
            graj()
        else:
            print("bye")
            exit()

    selected_so_far.append(x)
    zgaduj(letters, count, guessed_letters, selected_so_far)
        

def rysuj(guessed_letters = [], rys=""):
    for l in word:
        if l in guessed_letters:
            rys = rys + f"{l} "
        else:
            rys = rys + "-- "
    return rys
