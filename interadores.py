import sys
import time

lista = [0, 1, 2, 3, 4, 5]
lista = iter(lista)

print(next(lista))
print(next(lista))
print(next(lista))

print(hasattr(lista, '__next__'))

## geradores

l1 = [x for x in range(1000)] #iteravel
l2 = (x for x in range(1000)) #gerador

for v in l2:
    print(v)

def gera():
    for n in range(1000):
        yield n
        time.sleep(0.1)
g = gera()

print(g)
