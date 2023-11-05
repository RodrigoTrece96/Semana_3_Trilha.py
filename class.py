# Lembrete de boa prática: esquematize o projeto! 

class Padeiro: # O nome da classe tem que ser maíusculo 
    def __init__(self, nome): # Atributos
        self.nome = nome
        self.paes = 0
        self.dinheiro = 0
        pass

    def assar_paes(self, quantidade): # Métodos
        if quantidade > 6:
            print('A capacidade de assar pães está no limite')
        
        else: 
            self.paes += quantidade # Mesma coisa que self.paes = self.paes + quantidade
        pass

class Cliente:
    
    def __init__(self, nome, dinheiro): # Atributos
        self.nome = nome
        self.dinheiro = dinheiro
        self.paes = 0
        pass

    def comprar_paes(self, quantidade, Padeiro): # Métodos
        preco_pao = quantidade * 1.2

        if quantidade > Padeiro.paes: 
            print('Não há pão o suficiente para comprar')

        elif self.dinheiro < preco_pao:
            print('O dinheiro é insuficiente!')
            
        else:
            self.paes += quantidade
            self.dinheiro -= preco_pao
            Padeiro.dinheiro = preco_pao 
            Padeiro.paes -= quantidade 
            print(f'Compra realizada!\nO número de pães de {self.nome} é {self.paes}. \
O padeiro {padeiro1.nome} agradece e sua quantidade de pão restante é {padeiro1.paes}. Volte sempre!')
        pass 


padeiro1 = Padeiro('Jonathan')
padeiro1.assar_paes(6)
cliente1 = Cliente('Sérgia', 10)
cliente1.comprar_paes(5 ,padeiro1)