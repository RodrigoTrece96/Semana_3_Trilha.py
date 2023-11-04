# O que falta adicionar mais interações entre as pessoas: relacionar as interações com os atributos do __init__ e usar 
# condicionais para algumas interações  

# Os métodos vão ser troca de dinheiro, compra de drink e compra de comida, possivelmente


import random 


lugar = ('Mantiquira', 'SME', 'Santa Cruz da Serra', 'Mr.Copão', 'RioSul', 'Fundão', '485', 'Praia de Copa')


# Nome da classe sempre começa com letra maiuscula

class Pessoa1: 
    def __init__(self, nome): # Usar as descricoes para a conversa entre as pessoas                                            # Fixo para qualquer cenario (independente do lugar)
        self.nome = nome
        # self.apelido = apelido
        # self.idade = idade
        # self.comida_favorita = comida_favorita
        pass
    
    def encontro_1(self, hobbies, saidas_casuais, status_civil, dinheiro, drink, prato_escolhido):
        self.hobbies = hobbies
        self.saidas_casuais = saidas_casuais
        self.status_civil = status_civil
        self.dinheiro = dinheiro # Vai variar dependendo do lugar
        self.drink = drink 
        self.prato_escolhido = prato_escolhido
        pass

class Pessoa2():
    def __init__(self, nome, apelido, idade, comida_favorita): # Usar as descricoes para a conversa entre as pessoas
        self.nome = nome
        self.apelido = apelido
        self.idade = idade
        self.comida_favorita = comida_favorita
        pass
    
    def encontro_2(self, hobbies, saidas_casuais, status_civil, dinheiro, drink, prato_escolhido):
        self.hobbies = hobbies
        self.saidas_casuais = saidas_casuais
        self.status_civil = status_civil
        self.dinheiro = dinheiro # Vai variar dependendo do lugar
        self.drink = drink 
        self.prato_escolhido = prato_escolhido
        pass

def escolhendo_historinha(): 
    local_de_encontro = random.choice(lugar)
    print(f'Estão batendo um papo em {local_de_encontro}')
    return local_de_encontro 


local_de_encontro = escolhendo_historinha() # Desempacotado da tupla 


def caso_Mantiquira(local_de_encontro, Pessoa1, Pessoa2): # check
    if local_de_encontro == 'Mantiquira':
        print(f'Com licença, meu nome é {Pessoa1.nome}.')
        pass
    

def caso_SME(local_de_encontro, Pessoa1, Pessoa2): # check
    if local_de_encontro == 'SME':
        print(f'O trabalho hoje está cansativo! A propósito, meu nome é {Pessoa1.nome}.')
        pass


def caso_Santa_Cruz_da_Serra(local_de_encontro, Pessoa1, Pessoa2): # check
    if local_de_encontro == 'Santa Cruz da Serra':
        print(f'Que calor! O ar condicionado podia funcionar, né? Inclusive, prazer, meu nome é {Pessoa1.nome}.')
        pass


def caso_Mr_Copao(local_de_encontro, Pessoa1, Pessoa2): # check
    if local_de_encontro == 'Mr.Copão':
        print(f'Cara, aqui no posto 2 não tem restaurante melhor que o {local_de_encontro} por esse preço. Meu nome? Me chamo \
{Pessoa1.nome}, prazer!')
        pass 
    
    
def caso_Rio_Sul(local_de_encontro, Pessoa1, Pessoa2): # check
    if local_de_encontro == 'RioSul':
        print(f'Fala, mano! Meu nome é {Pessoa1.nome}. Quer dar um pulo no BK ou prefere ir no Outback?')
        pass


def caso_Fundao(local_de_encontro, Pessoa1, Pessoa2): # check
    if local_de_encontro == 'Fundão':
        print(f'Cara, eu recomendo sempre ir na Dona Graça e no Seu Augusto! Fica no segundo andar do bloco G. \
Ah mandei mal, meu nome é {Pessoa1.nome}, nem me apresentei.')
        pass


def caso_485(local_de_encontro, Pessoa1, Pessoa2): # check
    if local_de_encontro == '485':
        print(f'Bicho, toda vez que eu, {Pessoa1.nome}, pego o {local_de_encontro} algum evento cósmico acontece. É doideira.')
        pass


def caso_Praia_de_Copa(local_de_encontro, Pessoa1, Pessoa2): # check
    if local_de_encontro == 'Praia de Copa':
        print(f'Eu curto muito ficar aqui no posto 2, tem gente de todo tipo, isso é bacana! Me chamo {Pessoa1.nome} \
fico ali na Barata Ribeiro!')
        pass


Pessoa1.nome = 'Rodrigo' # Adicionar os atributos antes de chamar as funções. Caso contrário vai dar erro: atributo não especificado


# Chamando as funções para o primeiro teste:

caso_Mantiquira(local_de_encontro, Pessoa1, Pessoa2)
caso_SME(local_de_encontro, Pessoa1, Pessoa2)
caso_Santa_Cruz_da_Serra(local_de_encontro, Pessoa1, Pessoa2)
caso_Mr_Copao(local_de_encontro, Pessoa1, Pessoa2)
caso_Rio_Sul(local_de_encontro, Pessoa1, Pessoa2)
caso_Fundao(local_de_encontro, Pessoa1, Pessoa2)
caso_485(local_de_encontro, Pessoa1, Pessoa2)
caso_Praia_de_Copa(local_de_encontro, Pessoa1, Pessoa2) 


