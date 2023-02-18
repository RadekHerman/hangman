# from hangman_game.lang import hangman_EN, hangman_PL
from hangman_game.lang import hangman

import os

def main():
    os.system('clear')
    print("Welcome to HANGMAN.")
    print("Please choose language version of the game.")
    print('(1) for Polish, (2) for English')
    language = input("..: ").upper()
    if language == '1': 
        language = "PL"
        hangman.graj(language)
    elif language == '2': 
        language = "EN"
        hangman.graj(language)
    else:
        main()


if __name__ == '__main__':
    main()