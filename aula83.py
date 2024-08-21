"""
Condição If, ELif e else
"""

user = input('digite seu user: ')
qtd_caracteres = len(user)

if qtd_caracteres < 6:
    print('digite pelo menos 6 caracter')
else:
    print('voce foi cadastrado no sistema.')

string1 = input('digite: ')
string2 = input('digite: ')

print(f'total {len(string1) + len(string2)}')