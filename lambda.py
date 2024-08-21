"""
def funcao(arg, arg2):
    return  arg * arg2

var = funcao(2, 3)
print(var)

a = lambda x, y: x * y
print(a(2, 3))
"""

lista = [
    ['p1', 13],
    ['p2', 12],
    ['p3', 3],
    ['p4', 4],
]
#def func(item):
#    return item[1]

#lista.sort(key=lambda item: item[1], reverse=False)
#print(lista)

print(sorted(lista, key=lambda i: i[1]))