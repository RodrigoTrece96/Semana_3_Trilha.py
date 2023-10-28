list_01 = [i**2 for i in range(11)] #dentro da própria lista tem o iterator: código + sucinto

print(list_01)

list_02 = []

for i in range(11): # o iterator está fora da lista
    list_02.append(i**2)

print(list_02)


