"""
Função (def em Python - *args **kwargs
"""
def funcao(*args, **kwargs):
    print(args)
    print(args[0])
    print(len(args))
    print(kwargs)
    print(kwargs['nome'])

    nome = kwargs.get('nome')
    if nome is not None:
        print(nome)

funcao(1, 3, 4, nome='Allan', sbrenome='Inocencio')

def func(*args):
    for v in args:
        print(v)

def fun(*args):
    args = list(args)
    args[0] = 20

lista = [1,2,3,4,5]
print(*lista, sep='-')

lista1 = [1,23,34]
func(*lista1)