
"""
x = 0
while x < 9:

    y = 10
    while y > 2:
        y = y - 1
        print(f'{x} {y}')

    x += 1

"""
numeros = [10, 9, 8, 7, 6, 5, 4, 3, 2]

for n, y in enumerate(numeros):
    print(n, y)


dez = 10
oito = 0

while dez >= 2:
    print(oito, dez)
    dez = dez - 1
    oito += 1

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)