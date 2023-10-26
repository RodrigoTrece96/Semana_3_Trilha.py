# Refazendo o cronometro usando funções 

import time
import os

def unidades_cronometro(): # Aqui a função não possui parâmetro, pois dentro dela
    segundo = 0            #está uma variável fixa
    minuto = 0
    hora = 0
    return segundo, minuto, hora  


def conversao_unidades_cronometro(segundo, minuto, hora):
    if segundo == 60:
        segundo = 0
        minuto += 1

    if minuto == 60:
        minuto = 0 
        hora += 1 

    return segundo, minuto, hora

def formatacao_unidades(segundo, minuto, hora):
    if segundo < 10:
        segundo = f'0{(segundo)}'

    if minuto < 10:
        minuto = f'0{(minuto)}'
    
    if hora < 10:
        hora = f'0{(hora)}'
    
    print(f'{hora}:{minuto}:{segundo}')

def main():
    segundo, minuto, hora = unidades_cronometro()

    while True:

        os.system('clear')
        segundo, minuto, hora = conversao_unidades_cronometro(segundo, minuto, hora)
        formatacao_unidades(segundo, minuto, hora)

        time.sleep(1)
        segundo += 1 

main() # O main nao tem variavel intrinseca a ele: todas estão vido de outra 



    






    
    