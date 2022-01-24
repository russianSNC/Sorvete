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

# def ato1(): <-- futuramente 
    
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

sleep(4.00)
clear()

slprint('Eu sempre estarei observando', speed=0.10)

sleep(2.00)

slprint('Mas porque???')

sleep(4.00)

print(colored('\nisso nunca acaba', "red"))

print('eu to no meu proprio')

print(colored('l o o p    i n f e r n a l', "red"))

sleep(8.00)
clear()

sleep(2.00)
print(colored(ato1.center(37), "green"))
print(colored("\nTerra".center(37), "green"))

sleep(7.00)
clear()

slprint('???> ei ei, acorda,', speed=0.10)

slprint('???> ta na hora de vc levantar')

print('???> esta atrassada !')

sleep(4.00)
clear()

print(scott)
sleep(3.00)
slprint('Scott> Todo dia tenho que te acordar?')
print(colored('Scott> boa sorte na prova <3'))
sleep(7.00)
clear()

slprint('P R O V A ?', speed=0.20)
sleep(4.00)
clear()

print(morganawalkingtop)
slprint('que droga, esqueci disso serio')
sleep(3.00)
clear()
print(walk1)

sleep(3.00)
clear()