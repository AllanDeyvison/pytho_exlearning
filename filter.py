from dados import pessoas, produtos, lista

nova_lista = filter(lambda x: x > 5, lista)
#nova_lista = [x for x in lista if x > 5]
print(list(nova_lista))

li = filter(lambda p: p['preco'] > 50, produtos)

for produto in li:
    print(produto)