"""
Split, Join, Enumerate em Python
Split - dividir uma string #str
join - juntar uma lista #str
enumarate enumerar elementos da lista #list iteráveis
"""

string = 'O brasil é o pais do futebol, o brasil é penta.'
lista_1 = string.split(' ')
lista_2 = string.split(',')

#for valor in lista_1:
   # print( f' A palavra {valor} apareceu {lista_1.count(valor)} x na frase')
palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

for valor in lista_2:
    print(valor.strip().capitalize())

string = 'O Brasil é penta.'
lista = string.split(' ')
print(lista)
string = ' '.join(lista)
print(string)

for indice, valor in enumerate(lista, 13):
    print(indice, valor)

nomes = [
    ['Allan', 'Deyvison', 'Dias'],
    ['Ana', 'Paula', 'Almeida'],
    ['Ariane', 'Texeira', 'Oliveira']
]

for v1 in enumerate(nomes, 13):
    valor_enumerado, lista_nomes = v1
    nome1, nome2, nome3 = lista_nomes
    print(nome1)

