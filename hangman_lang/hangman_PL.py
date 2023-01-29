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
    print("Wybierz słownik:")
    print("(1) Polski lub (2) Angielski.")
  
    while True:
        letter_lang_choice = input("..:")
        if letter_lang_choice == "1":
            lineno = random.randint(1, 258995)  # ilość słów    
            word = (linecache.getline('slowa.txt', lineno)).strip().rstrip("/n").upper()
            break
        elif letter_lang_choice == "2":
            lineno = random.randint(1, 58110)  # ilość słów    
            word = (linecache.getline('words.txt', lineno)).strip().rstrip("/n").upper()
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
    print("+ W I S I E L E C +")
    print(" ++++++++++++++++")
    print()

def zgaduj(letters, count, guessed_letters, selected_so_far):  
    clear()
    print(wisielec[count])
    print()
    print(rysuj(guessed_letters))
    print()
    if lives-count > 1:
        print(f"Masz jeszcze {lives-count} prób, szubienica czeka.")
    else:
        print("OSTATNIA PRÓBA!  ")
    print()

    x = (input("podaj literę :")).upper()
    if x in letters:
        print("ODGADŁEŚ!!")
        letters.remove(x)
        guessed_letters.append(x)
    elif x in selected_so_far:
        print("Już wybierałeś tę literę, spróbuj jeszcze raz.\n")
        selected_so_far.sort()
        selected_so_far_str = ", ".join(selected_so_far)
        print(f"Te litery już wybierałeś: {selected_so_far_str} \n")
        input("Naciśnij dowolny klawisz aby kontynuować.")
        zgaduj(letters, count, guessed_letters, selected_so_far)
    else:
        count = count + 1
        print("NIE ODGADŁEŚ!")
        if count == lives:
            clear()
            print(wisielec[count])
            print(f"Koniec gry... odpowiedź : {word}")
            exit()        
    
    if len(letters) == 0:
        clear()
        print("GRATULACJE!!!!")
        print(wisielec[8])
        count = 0
        guessed_letters = []
        selected_so_far=[]
        czy = (input("Czy chcesz zagrać jeszcze raz? (t/n): ")).lower()
        if czy == 't':
            graj()
        else:
            print("pa")
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
