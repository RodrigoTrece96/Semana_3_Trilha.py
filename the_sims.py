# Ideia do projeto: duas pessoas podem se encontrar em locais aleatórios 
# (criar uma tupla com locais: Mr.Copão, RioSul, etc e depois escolher o lugar com o random.choice) 
# e para cada um dos locais
# as interações vão ser diferentes: em um bar elas vão sentar em uma mesa, conversar, comprar uma bebida
# escolher um petisco, etc - por exemplo. A interação pode ser feito a partir de condicionais e talvez loops
# A ideia é ter um script para cada cenário: uma historinha mesmo. Espero que essa ideia possa servir para 
# fixar o conteúdo de classes! 

class pessoa1:
    def __init__(self):
        self.cidade: ('Rio de Janeiro', 'Duque de Caxias')
        self.lugar: ('Mantiquira', 'SME', 'Santa Cruz da Serra', 'Mr.Copão', 'RioSul', 'Fundão', '485', 
                    'praia de copa')
    
    def descricoes(self, sexo, nome, apelido, idade, comida_favorita):
        self.tipo: sexo
        self.nome: nome
        self.apelido: apelido
        self.idade: idade
        self.comida_favorita: comida_favorita

    def tempo_livre_1(self, hobbies, saidas_casuais, status_civil, dinheiro):
        self.hobbies: hobbies
        self.saidas_casuais: saidas_casuais
        self.status_civil: status_civil
        self.dinheiro: dinheiro
    
    
