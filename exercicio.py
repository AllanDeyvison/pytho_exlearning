carrinho =[]

carrinho.append(('Camisa', 25.99))
carrinho.append(('Camisa', 25.99))
carrinho.append(('Camisa', 25.99))
carrinho.append(('Calça', 105.59))
carrinho.append(('Jacketa', 275.50))
carrinho.append(('Tênis', 645.90))

total = [s[1] for s in carrinho]
total2 = sum([float(y) for x, y in carrinho])

print(sum(total))

"""
total = []
for produto in carrinho:
    total.append(produto[1])

print(sum(total))
"""