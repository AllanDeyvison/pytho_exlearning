variavel = ['Allan', 'Deyvison', 'Inocencio']

primeira_letra = False
for valor in variavel:
    if valor.lower().startswith('a'):
        primeira_letra = True

if primeira_letra:
    print("Existe!")
else:
    print("Naõ")

for valor in variavel:
    if valor.lower().startswith('a'):
        break
else:
    print("Não")

