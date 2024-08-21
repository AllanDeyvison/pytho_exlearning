string = '01234567890123456789012345678901234567890123456789'

cont = [i for i in range(0, len(string), 10)]
tuplas = [(i,i +10) for i in range(0, len(string), 10)]
lista = [string[i:i +10] for i in range(0, len(string), 10)]
raw = [f'string[{i}:{i + 10}]' for i in range(0, len(string), 10)]

print(cont)
print(tuplas)
print(lista)
print('.'.join(lista))

"""
lista = [string[i:i+10] for i in range(0, len(string), 10)]
print('.'.join(lista))

print('9.'.join(string.split('9'))[:-1])
"""