from dados import pessoas, produtos, lista
from functools import reduce

'''
acumula = 0
for i in lista:
    acumula += i
print(acumula)
'''
soma_lista = reduce(lambda  ac, i: i + ac, lista, 0)
print(soma_lista)

soma_preco = reduce(lambda ac, i: i['preco'] + ac, produtos, 0)
print(soma_preco)

soma_idade = reduce(lambda  ac, i: i['idade'] + ac, pessoas, 0)
print(soma_idade / len(pessoas))