# Criando uma calculadora de pH em uma titulação ácido forte x base forte

import math

def concentracao_acido_base_do_sistema():

    concentracao_acido = 0.1000 #mol/L
    concentracao_base = 0.1000 #mol/L
    volume_acido = 20.00 #mL
    volume_base = float(input('Digite o volume de titulante lido na bureta >> '))
    
    return concentracao_acido, concentracao_base, volume_acido, volume_base

def calculando_nova_concentracao_acido(concentracao_acido, concentracao_base, volume_acido, volume_base):

    if volume_base != 0:
        moles_acido = concentracao_acido*volume_acido - concentracao_base*volume_base
        concentracao_acido = moles_acido/(volume_acido + volume_base)
 
    else:
        concentracao_acido = concentracao_acido

    
    return concentracao_acido, concentracao_base, volume_acido, volume_base

def calculando_pH_do_sistema():
    
    #Desempacotando os valores retornados até agora: vem na forma de tupla
    concentracao_acido, concentracao_base, volume_acido, volume_base = concentracao_acido_base_do_sistema()
    concentracao_acido, concentracao_base, volume_acido, volume_base = calculando_nova_concentracao_acido(concentracao_acido, concentracao_base, volume_acido, volume_base)

    if concentracao_acido != 0:
        pH = -1*math.log(concentracao_acido, 10)
        pH = round(pH, 2)
        print(f'O pH do meio é: {pH}')

    if concentracao_acido == 0:
        pH = 7.0
        print(f'Somente resta o equilíbrio da água, pH: {pH}')

    return pH 

calculando_pH_do_sistema()