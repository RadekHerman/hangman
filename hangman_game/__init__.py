from . import lang
from .game import main
from .lang import wisielec_print

# Make the `wisielec` dictionary available in the `hangman_game` namespace
wisielec = wisielec_print.wisielec
