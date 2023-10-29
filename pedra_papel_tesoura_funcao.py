import random
 
def condicoes_iniciais():
    rodada = 1
    score_usuario = 0
    score_computador = 0
    return rodada, score_usuario, score_computador

def jogadas_possiveis():
    possibilidades = ('pedra', 'papel', 'tesoura')
    jogada_usuario = input('Digite pedra, papel ou tesoura: ')
    jogada_computador = random.choice(possibilidades)
    
    if jogada_usuario not in possibilidades:
        print('Jogada inválida!')

    return possibilidades, jogada_usuario, jogada_computador

rodada, score_usuario, score_computador = condicoes_iniciais() # chamar a função aqui, pois se estiver dentro do while, 
                                                               # a cada iteração os valores voltariam para zero

while True:

    possibilidades, jogada_usuario, jogada_computador = jogadas_possiveis()

    print(f'Score >> {score_usuario}:{score_computador}')
    print(f'Rodada: {rodada}')  

    if score_usuario == 3 or score_computador == 3:
        print(f'A partida acabou. O score ficou: {score_usuario}:{score_computador} e o número de rodadas foram {rodada}')
        break 

    # Caso em que empata
    if jogada_usuario == jogada_computador: 
        print('Empate')
        rodada += 1
        continue # fato legal sobre o continue: ele evita que coisas do loop que não serão importantes para aquela iteração 
                 # sejam lidas pelo código. Então deixa a leitura do código mais sucinta e efetiva 

    # Caso em que o jogador vence
    if (jogada_usuario == 'pedra' and jogada_computador == 'tesoura') or \
        (jogada_usuario == 'papel' and jogada_computador == 'pedra') or \
        (jogada_usuario == 'tesoura' and jogada_computador == 'papel'):
        print('Você venceu!')
        rodada += 1 
        score_usuario += 1
        continue
           

    # Caso em que o computador vence
    if (jogada_computador == 'pedra' and jogada_usuario == 'tesoura') or \
        (jogada_computador == 'papel' and jogada_usuario == 'pedra') or \
        (jogada_computador == 'tesoura' and jogada_usuario == 'papel'):
        print('O computador venceu!')
        rodada += 1
        score_computador += 1
        continue