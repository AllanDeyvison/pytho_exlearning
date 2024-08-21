# add (adiciona), update (atualiza), clear, discard
# union |
# intersection & (todos elementos presentes nos dois sets
# difference - (elementos apenas o set da esquerda)
# symmetric_difference ^ ( elementos que estão nos dois sets, mas não em ambos)

#lista = [3, 2, 1, 8, 4, 7, 9, 5, 7, 10]
#p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l = [
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
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]
for po, li in enumerate(l):
    lista = l[po]

    def funcao():
        for p, n in enumerate(lista):
            for x, num in enumerate(lista):
                # print(p, x, '|', n, num)
                if p == x:
                    n = 0
                if n == num:
                    return num
    if funcao() != None:
        print(funcao())
    else:
        print(-1)



"""
def funcao():
    for p, l in enumerate(lista):
        for po, n in enumerate(lista[p]):
            for x, num in enumerate(lista[p]):
                #print(p, x, '|', n, num)
                if po == x:
                    n = 0
                if n == num:
                    print(num)
"""

"""
def funcao():
    for p, n in enumerate(lista):
        for x, num in enumerate(lista):
           # print(p, x, '|', n, num)
            if p == x:
                n = 0
            if n == num:
                return num
                break
"""

"""
for p, n in enumerate(lista):
    for x, num in enumerate(lista):
        print(p, x, '|', n, num)
        if n == num and p != x:
            print("--------------------", num)
            break
"""
"""
for po in p:
    v = po + 1
    if v == 10:
        break
    elif lista[po] == lista[v]:
        print(lista[v])
"""