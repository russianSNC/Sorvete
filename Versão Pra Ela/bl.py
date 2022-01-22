from time import sleep
import sys
import os
from colorama import Fore

def beautifulPrint(text: str, color='WHITE', instaPrint=None, delay=0.1, instaDelay=0.5):

    # o if abaixo é FALSE se instaPrint=None, 
    # agora, se instaPrint for uma string 
    # (ou tiver um valor) ele vai executar o if em questão.
    if instaPrint: 
        sys.stdout.write(getattr(Fore, color)+instaPrint+' ')
        sys.stdout.flush()

    sleep(instaDelay)

    # criando loop para printar char por char
    for i in text:
        # delay de print
        sleep(delay) 
        # enviando para o output uma caractere com cor de COLOR 
        # usando getattr de Fore com nome de COLOR (Fore.COLOR)
        sys.stdout.write(getattr(Fore, color)+i) 
        # enviando o output para o prompt
        sys.stdout.flush()