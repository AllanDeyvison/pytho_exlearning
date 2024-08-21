"""
Zip - unindo iteráveis
zip_longest - Itertools
"""
from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Londres', 'Los Angeles', 'Salvador']

paises = ['BR', 'UK', 'USA']

#paise_cidades = zip_longest(paises, cidades, fillvalue='Estado')
paise_cidades = zip(
    indice,
    paises,
    cidades,

)

for indice, paises, cidades in paise_cidades:
    print(indice, paises, cidades)

variavel = ((x,y) for x,y in zip('Alo', 'Alo'))