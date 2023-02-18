import random
import linecache
import os
import time
from .wisielec_print import wisielec
import pathlib

# Get the path to the directory containing this file
module_path = pathlib.Path(__file__).resolve().parent

# Get the path to the text file relative to the module directory
slowa_file_path = module_path / 'slowa.txt'
words_file_path = module_path / 'words.txt'


output_strings = {
    "PL": {
        "choose_dict": "Wybierz słownik z którego zostanie pobrane słowo.\n(1) Polski lub (2) Angielski.",
        "banner": " +++++++++++++++++\n+ W I S I E L E C +\n ++++++++++++++++\n\n",
        "lives": "Szubienica czeka.. Pozostało prób:",
        "last_chance": "OSTATNIA PRÓBA!",
        "guess_letter" : "Podaj literę: ",
        "guessed": "ODGADŁEŚ!!",
        "already_taken": "Już wybierałeś tę literę, spróbuj jeszcze raz.\n",
        "guesses": "Wybierane do tej pory: ",
        "press_any": "Naciśnij dowolny klawisz aby kontynuować.",
        "not_guessed": "NIE ODGADŁEŚ!",
        "end" : "Koniec gry... odpowiedź:",
        "congrat": "GRATULACJE!!!!",
        "play_again": "Czy chcesz zagrać jeszcze raz? (t/n): ",
        "yes": "t",
        "bye": "pa",
    },
    "EN": {
        "choose_dict": "Please choose the dictionary:\n(1) Polish or (2) English.",
        "banner": " +++++++++++++++++\n + H A N G M A N +\n ++++++++++++++++\n\n",
        "lives": "The gallows is waiting. The lives left:",
        "last_chance": "The Last Chance!",
        "guess_letter" : "Guess the letter: ",
        "guessed": "YOU GUESSED!!",
        "already_taken": "You have already chosen that letter, please try again.\n",
        "guesses": "The letters you have tried so far: ",
        "press_any": "Press any key.",
        "not_guessed": "NOT GUESSED!!",
        "end" : "Game over... word: ",
        "congrat": "CONGRATULATIONS!!!!",
        "play_again": "Do you want to play again? (y/n): ",
        "yes": "y",
        "bye": "bye",
    }

}




def graj(language):
    global output
    output = output_strings[language]
    global word
    global lives
    count = 0
    guessed_letters = []
    selected_so_far = []
    lives = 7 
    clear()
    print(output["choose_dict"])

    while True:
        letter_lang_choice = input("..:")
        if letter_lang_choice == "1":
            lineno = random.randint(1, 258995)  # ilość słów    
            word = (linecache.getline(str(slowa_file_path), lineno)).strip().rstrip("/n").upper()
            break
        elif letter_lang_choice == "2":
            lineno = random.randint(1, 58110)  # ilość słów    
            word = (linecache.getline(str(words_file_path), lineno)).strip().rstrip("/n").upper()
            break
        else:
            pass

    letters = set(word)
    zgaduj(letters, count, guessed_letters, selected_so_far)

def clear():
    time.sleep(2)
    os.system('clear')
    time.sleep(0.5)
    print(output["banner"])

def zgaduj(letters, count, guessed_letters, selected_so_far):  
    clear()
    print(wisielec[count])
    print()
    print(rysuj(guessed_letters))
    print()
    if lives-count > 1:
        print(f"{output['lives']} {lives-count}")
    else:
        print(output["last_chance"])
    print()

    x = (input(output["guess_letter"])).upper()
    if x in letters:
        print(output["guessed"])
        letters.remove(x)
        guessed_letters.append(x)
    elif x in selected_so_far:
        print(output["already_taken"])
        selected_so_far.sort()
        selected_so_far_str = ", ".join(selected_so_far)
        print(f"{output['guesses']} {selected_so_far_str} \n")
        input(output["press_any"])
        zgaduj(letters, count, guessed_letters, selected_so_far)
    else:
        count = count + 1
        print(output["not_guessed"])
        if count == lives:
            clear()
            print(wisielec[count])
            print(f"{output['end']} {word}")
            exit()        
    
    if len(letters) == 0:
        clear()
        print(output['congrat'])
        print(wisielec[8])
        count = 0
        guessed_letters = []
        selected_so_far=[]
        czy = (input(output["play_again"])).lower()
        if czy == output["yes"]:
            graj()
        else:
            print(output["bye"])
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
