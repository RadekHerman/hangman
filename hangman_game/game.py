from hangman_game.lang import hangman_EN, hangman_PL

import os

def main():
    os.system('clear')
    print("Welcome to HANGMAN.")
    print("Please choose language version of the game.")
    print('(P) for Polish, (E) for English, ')
    language = input("..: ").upper()
    if language == 'P':
        hangman_PL.graj()
    elif language == 'E':
        hangman_EN.graj()
    else:
        main()


if __name__ == '__main__':
    main()