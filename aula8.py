"""
For in Python
Iterando strings com format(Função range(star=0, stop, step=1)
"""

for n in range(20,10,-1):
    print(n)

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra

print(nova_string)