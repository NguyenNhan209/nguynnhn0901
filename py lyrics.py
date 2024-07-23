import sys
from time import sleep
import time
import os
import pygame
from colorama import init, Fore, Style

init(autoreset=True)

COLORS_STYLES = {
    'red': Fore.RED,
    'green': Fore.GREEN,
    'yellow': Fore.YELLOW,
    'blue': Fore.BLUE,
    'magenta': Fore.MAGENTA,
    'cyan': Fore.CYAN,
    'white': Fore.WHITE,
    'light_red': Fore.LIGHTRED_EX,
    'light_green': Fore.LIGHTGREEN_EX,
    'light_yellow': Fore.LIGHTYELLOW_EX,
    'light_blue': Fore.LIGHTBLUE_EX,
    'light_magenta': Fore.LIGHTMAGENTA_EX,
    'light_cyan': Fore.LIGHTCYAN_EX,
    'light_white': Fore.LIGHTWHITE_EX,
    'dim': Style.DIM,
    'normal': Style.NORMAL,
    'bright': Style.BRIGHT,
    'reset': Style.RESET_ALL
}

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load('E:/2110ChillMusic/In the shadow of the sun .mp3')
    pygame.mixer.music.play(-1)

def in_lyrics():
    play_music()
    os.system('cls')
    lines = [("And i'ii waiting in the shadow of the sun",0.09,'red','bright'),
             ("Seizing time where no one's been before",0.1,'blue','normal'),
             ("Close the curtains what you waiting for?",0.09,'yellow','dim'),
             ("And I'ii be keeping",0.1,'green','bright'),
             ("Secrets",0.1,'magenta','normal'),
             ("Till im in the ground",0.15,'red','bright')]
    
    delays = [0.1, 0.1, 0.1, 0.1, 0.1, 0.12, 0.5]

    for i, (line, char_delay, color, style) in enumerate(lines):
        for char in line:
            print(f"{COLORS_STYLES[style]}{COLORS_STYLES[color]}{char}{COLORS_STYLES['reset']}", end="")
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

in_lyrics()
sleep(3)
