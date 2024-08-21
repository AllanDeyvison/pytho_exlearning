
#!/usr/bin/env python

"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
#         0    1    2
lista = ['A', 'B', 'C']
#         -3   -2  -1
print(lista[2:])

l1 =[1,2,3]
l2 =[4,5,6]
l3 = l1 + l2
l1.extend(l2)

l2.append('b')
l2.insert(0,'banana')
#l2.pop() deleta o ultimo
#del(l2[3:5])
l2 = list(range(0,100, 8))

for valor in l1:
    print(valor)

print( max(l2))
print( min(l2))

print(l1)
print(l2)
print(l3)
