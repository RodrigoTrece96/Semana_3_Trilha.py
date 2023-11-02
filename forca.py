# Forca no python 

import random

def condicoes_iniciais(): # Desempacotado
    possibilidades = ('loki', 'valk', 'engenharia', 'biotecnologia', 'pedagogia', 'guitarra')
    palavra = random.choice(possibilidades)
    return palavra

palavra = condicoes_iniciais()

def tamanho_palavra():
    tamanho = '_' * len(palavra) 
    return tamanho


def andamento_jogo():
    rodada = 0
    return rodada



while True:

    tamanho = tamanho_palavra()
    rodada = andamento_jogo()

    print(palavra)
    print(f'Esse é o número de letras da palavra: {tamanho}')
    print(f'Rodada: {rodada}')
    jogada_usuario = input('Digite uma letra: ').lower()

    if rodada > 8:
        print('As tentavivas acabaram. Fim de jogo!')
        break 

# Falta descobrir como trocar o '_' pela letra! 