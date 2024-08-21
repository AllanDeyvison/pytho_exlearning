lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

#d1 = {x: y*2 for x,y in lista}
#d2 = {x: y*2 for x,y in enumerate(range(5))}
#d2 = {x for x in range(5)} cria um set não um dic
d2 = {f'chave{x}': x**2 for x in range(5)}
print(d2)