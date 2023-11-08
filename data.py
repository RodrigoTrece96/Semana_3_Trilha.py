# Nota: antes estava dando erro porque o nome do arquivo era o mesmo nome da biblioteca
# O erro era "circular import" 

import pandas as pd

data = pd.read_csv('teste.csv')

rows = data.head(3) # por default: 5
rows2 = data.tail(2) # por default: 5

#print(data)

counting = data.count('index') #conta quantos rows tem o DataFrame
counting2 = data.count('columns') #conts quantas colunas tem o DataFrame
print(counting, counting2)





