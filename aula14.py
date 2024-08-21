nomes = [
    ['Allan', 'Deyvison', 'Dias'],
    ['Ana', 'Paula', 'Almeida'],
    ['Ariane', 'Texeira', 'Oliveira']
]

nome1, nome2, nome3 = nomes
nome1, nome2, *outra_lista, ultimo = nomes
nome1, nome2, *_ = nomes
print(nome1)

"""
z = x
x = y
y = z
"""

x = 10
y = 'Luiz'
z = 'Allan'
x, y = z,y, x

print(f'x={x} e y = {y} e z ={z}')


logged = False
msg = 'Usuario logado.' if logged else 'Usuario precis logar.'

print(msg)

idade = 18
maior = (idade >= 18)
msg = 'Pode acessar' if maior else 'Não pode acessar.'

print(msg)

nome1 = input('Nome:')
print(nome1 or 'vc n digitou nada!')

a = 0
b = None
c = False
d = 21
e = ' Allan'

variavel = a or b or c or d or e

print(variavel)