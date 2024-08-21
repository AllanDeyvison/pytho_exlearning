"""
d1 = {'chave1': 'valor da chave'}
d1['chave2'] = 'chave dois'

print(d1['chave1'])
"""

d1 = dict(chave1='Valor da chave', chave2='Valor da outra chave')
d1['nova_chave'] = 'Valor nova chave'

print('chave1' in d1)
print('chave1' in d1.keys())
print('chave1' in d1.values())
print(len(d1))
d1.pop('chave1')
d1.popitem('chave1') # elimina a ultima chave

del d1['chave1']
v = d1.copy()

d1.get('nomedachave')

print(d1)

for k, v in d1.items():
    print(k, v)

clientes = {
    'cliente1' : {
        'nome': ' Allan',
        'sobrenome': 'Inocencio',
    },
    'cliente2' : {
        'nome': ' Allan',
        'sobrenome': 'Inocencio',
    },
}


for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dado_v in clientes_v.items():
        print(f'\t{dados_k} = {dado_v}')