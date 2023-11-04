# Adicionar funcionalidade de dica: se pedir dica, cai em uma condicional que printa
# uma explicação geral do que a palavra está relacionada

import random

def condicoes_iniciais(): # Desempacotado

    possibilidades = ('processos', 'computador', 'engenharia', 'biotecnologia', 'pedagogia', 'guitarra', 'industria', 'quimica', 
    'cachorro', 'gato', 'mate', 'sushi')

    palavra = random.choice(possibilidades)
    rodada = 0
    return palavra, rodada

palavra, rodada = condicoes_iniciais()

def andamento_jogo(): # Desempacotado 
    tamanho = '_' * len(palavra) 
    letras_corretas = [] # Aqui serao adicionadas as letras corretas  
    return tamanho, letras_corretas

tamanho, letras_corretas = andamento_jogo()

numero_letras = tamanho.count('_')
print(f'O número de letras é: {numero_letras}')

print(f'O tamanho da palavra é: {tamanho}')

print('Instruções: caso você saiba a resposta antes, digite: "chute" ')

while True:

    rodada += 1

    print(f'Rodada: {rodada}')
    jogada_usuario = input('Digite uma letra: ').lower()

    if jogada_usuario in palavra:
        letras_corretas.append(jogada_usuario)
    
    palavra_usuario = ""

    for letra in palavra:
        if letra in letras_corretas:
            palavra_usuario += letra # Aqui tem que ser letra, caso seja jogada_usuario, a cada iteração a letra que ele escolheu vai para a string!!!
        
        else:
            palavra_usuario += '_'

    print(f'Seu progresso está assim: {palavra_usuario}')
    
    if jogada_usuario == 'chute':
        jogada_usuario = input('Digite seu chute: ').lower()
        if jogada_usuario == palavra:
            print('Parabéns, você venceu de forma antecipada!')
        else:
            print('Que pena, o chute estava incorreto!')
        break 
           
    if palavra_usuario == palavra:
        print('Parabéns, você venceu!')
        break

    if rodada == 20: # Final da partida
        print(f'As tentativas acabaram! A palavra correta era {palavra}. Foi uma boa rodada!')
        break 