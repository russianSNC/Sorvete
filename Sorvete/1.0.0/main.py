# Ok, vamos lá fazer o 2
# To fazendo isso por ela e por mim agora


# Game Imports
from colorama import init
from termcolor import colored
from os import system as s
from random import randint
from time import sleep
import sys
import os
from bl import *
import random as r

init()

# Começo da Main

beautifulPrint(text="A Muito Tempo atrás")

sleep(4.00)
s('cls')

# mixer.music.load("file.mp3") <---- musica pro futuro

beautifulPrint(text="uma garota")

sleep(4.00)
s('cls')

sleep(2.00)
print(colored('Caiu No Poço', "red"))
sleep(4.50)

s('cls')

# Final do prologo

print(colored("""

 ██████╗ █████╗ ██████╗ ██╗   ██╗███████╗████████╗███████╗
██╔════╝██╔══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔════╝
╚█████╗ ██║  ██║██████╔╝╚██╗ ██╔╝█████╗     ██║   █████╗  
 ╚═══██╗██║  ██║██╔══██╗ ╚████╔╝ ██╔══╝     ██║   ██╔══╝  
██████╔╝╚█████╔╝██║  ██║  ╚██╔╝  ███████╗   ██║   ███████╗
╚═════╝  ╚════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝ A Jornada infinita""", "magenta"))

beautifulPrint(text="depois de anos ela nunca entendeu oq aconteceu")
sleep(2.00)
print('\nnão lembra de nada, só sensações da sua morte')

print(colored('\nPor: ImPeterWA', "red"))

print("""
Comandos: 
-> Novo Jogo
-> Sair
-> Agradecimentos
-> ??? """)

# Fim do Menu, Começo das opções

choice = input("?: ")

if choice.lower() == "sair":
    quit()


if choice.lower() == "novo jogo":
    s('cls')
    print('teste')
    sleep(9.00)
    s('cls')