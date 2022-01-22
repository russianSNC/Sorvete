# Ok, vamos tentar isso...

# novamente, game imports

from colorama import init
from termcolor import colored
from os import system, name
from time import sleep
from PyInquirer import prompt
from examples import custom_style_1
from pyfiglet import Figlet

# Ascii Arts

from headers import *

# Funções Misc

fig = Figlet(font="big")

def slprint(text, speed=0.07):
    for i in text:
        print(i, end='', flush=True)
        sleep(speed)
    print('\n', end='')

def clear():
    _ = "cls" if name == "nt" else "clear"
    system(_)

# =============================================================================

init()

def ato1():
    
    slprint('Como Sair? Como Sair?.', speed=0.10)

    clear()

    slprint('Como Sair? Como Sair?.', speed=0.10)

    clear()

    slprint('Como Sair? Como Sair? Como Sair? Como Sair? Como Sair? Como Sair?.', speed=0.05)

    for i in range(0,10):
        sleep(0.05)
        print(colored('COMO SAIR?!', "red"))

    clear()

    print(closeface)
    slprint('Sim eu me perdi, eu to aqui dnv', speed=0.10)

    clear()

    print(olho)

    slprint('Eu sempre estarei observando', speed=0.10)

    sleep(4.00)

    clear()
