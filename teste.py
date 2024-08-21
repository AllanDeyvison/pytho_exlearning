matrix_de_inteiros = [
    [4, 2, 3, 66, 5, 6, 7, 8, 9, 3],
    [1, 2, 54, 4, 88, 6, 7, 8, 1, 6],
    [6, 54, 3, 4, 5, 5, 7, 8, 9, 93],
    [1, 2, 3, 9, 232, 6, 543, 8, 9, 5],
    [1, 2, 3, 1, 5, 6, 7, 83, 9, 6],
    [8, 32, 3, 43, 5, 65, 7, 82, 9, 9],
    [76, 15, 3, 7, 5, 6, 7, 7, 10, 7]
]

numero_duplicado = []


def numeros_duplicados(lista):
    for i in range(len(lista)):
        for v in range(len(lista[i])):
            if lista[i][v] is lista[i][v - 1]:
                numero_duplicado.append(lista[i][v])
    return numero_duplicado


resultado = numeros_duplicados(matrix_de_inteiros)
print(resultado)

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
]

encontrei = False
numero_lista = 1
index = 0

for lista in lista_de_listas_de_inteiros:
    print(f'{numero_lista}º Lista:')

    for valor in lista:
        # index < 9 - para não buscar o item lista[11].
        # valor == lista[index + 1] - para verificar se há a repetição.
        # encontrei is False - para pegar apenas a primeira repetição.
        if index < 9 and valor == lista[index + 1] and encontrei is False:
            print(valor, '\n')
            encontrei = True
        # Incremento o próximo index da lista que iremos comparar
        index += 1
    # Reseto os parâmetros para a próxima lista
    numero_lista += 1
    encontrei = False
    index = 0


