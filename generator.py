# entendo o generator e uma função: yield e return

tupla = (1,2,3,4,5)

def generator(tupla):
    for i in tupla:
        yield i**2 #quando o loop é retomado, começa-se do yield

g = generator(tupla)

for i in range(5):
    print(next(g))
