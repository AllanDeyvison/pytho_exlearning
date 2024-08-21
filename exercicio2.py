def saudacao(msg='Olá', nome='user'):
    return print(msg, nome)

msg = input('Coleque uma saudação: ')
nome = input('Coloque o seu nome: ')

saudacao(msg, nome)

def soma(num1, num2, num3):
    soma = num1 + num2 + num3
    return soma

num1 = input('Número: ')
num1 = int(num1)
num2 = input('Número: ')
num2 = int(num2)
num3 = input('Número: ')
num3 = int(num3)

print(soma(num1, num2, num3))