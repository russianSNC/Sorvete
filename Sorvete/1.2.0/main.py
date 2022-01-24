# Ok, vamos lá fazer o 2
# To fazendo isso por ela e por mim agora

# zewo mewa passou por aqui

# Changelog:
    # Removido imports redundantes
    
    # Funções clear e slprint adicionadas
        # slprint é um remake do beautifulPrint, sem dependências
        # clear possibilita a limpeza do console em ambos sistemas linux e windows, sem precisar escrever s('cls')

    # PyInquirer implementado
        # vai ser responsável por qualquer prompt
        # pode ser customizado (cores) e é flexível
        # sei la mano to bebadokkkkkkkkkkkkkkkkkkkkkkkkkk
    

# Game Imports
from colorama import init
from termcolor import colored
from os import system, name
from time import sleep
from PyInquirer import prompt
from examples import custom_style_1
from pyfiglet import Figlet
from agradecimentos import agradecer

init()

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

# Funções do menu/importantes

def prologue(part2=False):
    if not part2:
        clear()
        slprint(text="A Muito Tempo atrás...")
        sleep(1.60)

        # mixer.music.load("file.mp3") <---- musica pro futuro

        slprint(text="Uma garota...")
        sleep(1.60)

        print(colored('Caiu no poço.', "red"))
        sleep(2.00)

    else:
        slprint(text="Depois de anos, ela nunca entendeu o que aconteceu...", speed=0.05)
        sleep(1.50)
        slprint('Não lembra de nada, só sensações da sua morte.', speed=0.05)


def menu(first_time=False):
    if first_time: prologue()

    clear()
    print(colored(f"{fig.renderText('Sorvete')}", "magenta"), end='')
    print(colored("A Jornada infinita".center(37), "magenta"), end='\n\n')
    if first_time: prologue(True)

    print(colored('Feito por: ImPeterWA\n', "red"))

        # eu vou tentar meu melhor pra explicar o que caralhos tudo isso embaixo faz
        # a variável question é uma lista de um dicionário, cada prompt representa
        # um dicionário, assim, cada prompt pode ser configurado de forma diferente
        # o primeiro prompt do jogo é um do tipo list, apresentando uma lista de
        # possíveis escolhas para o jogador, as mesmas sendo: Novo Jogo,
        # Agradecimentos, ???, Sair, o jogador pode selecionar estas opções utilizando
        # as setinhas e pressionando enter, a variável question é apenas responsável
        # pelas questões, não pelas respostas. A variável answer é responsável
        # pelas mesmas, assim, é necessário acessar cada resposta de cada questão
        # de modo diferente, a propriedade name dentro de cada questão na variável
        # question é responsável por nomear as respostas, quando o usuário responder
        # esta pergunta, o resultado da mesma será salva na variável answer, com o
        # nome "choice", por isso é necessário acessá-la da forma asnwer['choice']

    question = [{
            'type': 'list',
            'name': 'choice',
            'message': 'Selecione uma opção:\n',
            'choices': ['Novo Jogo', 'Agradecimentos', '???', 'Sair'],
            'filter': lambda val: val.lower()
    }]

    answer = prompt(question, style=custom_style_1)

    # condições responsáveis pelo funcionamento do menu
    # russo continua as importantes

    if answer['choice'] == 'novo jogo':
        # russo continua daqui
        pass

    elif answer['choice'] == 'agradecimentos':
        agradecer()
        menu()

    elif answer['choice'] == '???':
        # russo continua daqui
        pass

    elif answer['choice'] == 'sair':
        quit()

# realmente iniciando o jogo
menu(True)


