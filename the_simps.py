# O que falta adicionar mais interações entre as pessoas: relacionar as interações com os atributos do __init__ e usar 
# condicionais para algumas interações  

# Os métodos vão ser troca de dinheiro, compra de drink e compra de comida, possivelmente


import random 
import time 


lugar = ('Mantiquira', 'SME', 'Santa Cruz da Serra', 'Mr.Copão', 'RioSul', 'Fundão', '485', 'Praia de Copa')


# Nome da classe sempre começa com letra maiuscula

class Pessoa1:
    def __init__(self, nome, status_civil, dinheiro, drink, prato_escolhido): # Usar as descricoes para a conversa entre as pessoas                                            # Fixo para qualquer cenario (independente do lugar)
        self.nome = nome
        self.hobbies_possibilidades = ('correr', 'dançar', 'viajar', 'cantar')
        self.saidas_casuais = ('orla da praia', 'aula de dança', 'aeroporto', 'show')
        self.status_civil = status_civil
        self.dinheiro = dinheiro            # Dependendo do drink que a pessoa escolher, vai ser gasto mais dinheiro!
        self.drink = drink                  # Essa parte é legal ser input: "what's your drink of choice" - Emma Darcy 
        self.prato_escolhido = prato_escolhido
        pass
        # self.apelido = apelido
        # self.idade = idade
        # self.comida_favorita = comida_favorita
        pass
    
    def definindo_possibilidades(self):
        self.hobbie = random.choice(self.hobbies_possibilidades) 

        

class Pessoa2():
    def __init__(self, nome): # Usar as descricoes para a conversa entre as pessoas
        self.nome = nome
        self.hobbies_possibilidades = ('correr', 'dançar', 'viajar', 'cantar')
        self.saidas_casuais = ('orla da praia', 'aula de dança', 'aeroporto', 'show')
        # self.apelido = apelido
        # self.idade = idade
        # self.comida_favorita = comida_favorita
        pass
    
    def encontro_2(self, status_civil, dinheiro, drink, prato_escolhido):
        self.status_civil = status_civil
        self.dinheiro = dinheiro  
        self.drink = drink 
        self.prato_escolhido = prato_escolhido
        self.hobbie = random.choice(self.hobbies_possibilidades)
        pass

# Adicionar os atributos antes de chamar as funções. Caso contrário vai dar erro: atributo não especificado
pessoa1 = Pessoa1('Rodrigo') 
pessoa1.encontro_1 = ('Solteiro', 13, 'Negroni', 'Sushi')
pessoa2 = Pessoa2('Mariana')
pessoa2.encontro_2 = ('Solteira', 12, 'Caipirinha', 'Pizza')

def escolhendo_historinha(pessoa1, pessoa2): 
    local_de_encontro = random.choice(lugar)
    print(f'Estão batendo um papo em {local_de_encontro}')
    print(f'Hobbie Pessoa1: {pessoa1.hobbie} e Hobbie Pessoa2: {pessoa2.hobbie}')
    return local_de_encontro

local_de_encontro = escolhendo_historinha(pessoa1, pessoa2) # Desempacotado da tupla 


def caso_Mantiquira(local_de_encontro, pessoa1): # adicionando acontecimentos 
    if local_de_encontro == 'Mantiquira':
        print(f'Com licença, meu nome é {pessoa1.nome}.') # parte padrão do encontro: tentar otimizar ao inves de ficar 
        print(f'O meu é {pessoa2.nome}, prazer!')         # em todas as funções 
        time.sleep(3) # Pausa para ficar mais organica a conversa
        print('Após alguns minutos de conversa...')
        pass 

    if pessoa1.hobbie == pessoa2.hobbie:
        print(f'Meu hobbie é {pessoa1.hobbie}.')
        print('Sério? o meu também é!')
        time.sleep(1)
        pass

    if pessoa1.hobbie == 'correr': 
        print(f'Meu hobbie é {pessoa1.hobbie}.')
        print(f'Ah, bacana! Você deve curtir {pessoa1.saidas_casuais}, né?')
        print('Nossa. Exatamente!')
        time.sleep(1)
        pass
    
    if pessoa1.hobbie == 'dançar':
        print(f'Meu hobbie é {pessoa1.hobbie}.')
        print(f'Pô, bacana! Você gosta de ir em {pessoa1.saidas_casuais}?')
        print(f'Sim! Gosto bastante. Meu objetivo é ser dançarina!')
        time.sleep(1)
        pass

    if pessoa1.hobbie == 'viajar':
        print(f'Meu hobbie é {pessoa1.hobbie}!')
        print(f'Nossa! Eu tenho muita vontade de conhecer o Egito!')
        print(f'Essa vai ser minha próxima viajem. Sempre quis visitar lugar históricos.')
        time.sleep(1)
        pass

    if pessoa1.hobbie == 'cantar':
        print(f'Meu hobbie é {pessoa1.hobbie}') 
        print(f'Que maneiro!')
        artista_preferido = input('Qual é o seu cantor favorito?')
        artista_preferido += artista_preferido  
        print('Eu também gosto bastante suas músicas!')
        time.sleep(1)
        pass


def caso_SME(local_de_encontro, pessoa1): # check
    if local_de_encontro == 'SME':
        print(f'O trabalho hoje está cansativo! A propósito, meu nome é {pessoa1.nome}.')
        pass


def caso_Santa_Cruz_da_Serra(local_de_encontro, pessoa1): # check
    if local_de_encontro == 'Santa Cruz da Serra':
        print(f'Que calor! O ar condicionado podia funcionar, né? Inclusive, prazer, meu nome é {pessoa1.nome}.')
        pass


def caso_Mr_Copao(local_de_encontro, pessoa1): # check
    if local_de_encontro == 'Mr.Copão':
        print(f'Cara, aqui no posto 2 não tem restaurante melhor que o {local_de_encontro} por esse preço. Meu nome? Me chamo \
{pessoa1.nome}, prazer!')
        pass 
    
    
def caso_Rio_Sul(local_de_encontro, pessoa1): # check
    if local_de_encontro == 'RioSul':
        print(f'Fala, mano! Meu nome é {pessoa1.nome}. Quer dar um pulo no BK ou prefere ir no Outback?')
        pass


def caso_Fundao(local_de_encontro, pessoa1): # check
    if local_de_encontro == 'Fundão':
        print(f'Cara, eu recomendo sempre ir na Dona Graça e no Seu Augusto! Fica no segundo andar do bloco G. \
Ah mandei mal, meu nome é {pessoa1.nome}, nem me apresentei.')
        pass


def caso_485(local_de_encontro, pessoa1): # check
    if local_de_encontro == '485':
        print(f'Bicho, toda vez que eu, {pessoa1.nome}, pego o {local_de_encontro} algum evento cósmico acontece. É doideira.')
        pass


def caso_Praia_de_Copa(local_de_encontro, pessoa1): # check
    if local_de_encontro == 'Praia de Copa':
        print(f'Eu curto muito ficar aqui no posto 2, tem gente de todo tipo, isso é bacana! Me chamo {pessoa1.nome} \
fico ali na Barata Ribeiro!')
        pass

# Chamando as funções para o primeiro teste:
caso_Mantiquira(local_de_encontro, pessoa1)
caso_SME(local_de_encontro, pessoa1)
caso_Santa_Cruz_da_Serra(local_de_encontro, pessoa1)
caso_Mr_Copao(local_de_encontro, pessoa1)
caso_Rio_Sul(local_de_encontro, pessoa1)
caso_Fundao(local_de_encontro, pessoa1)
caso_485(local_de_encontro, pessoa1)
caso_Praia_de_Copa(local_de_encontro, pessoa1) 