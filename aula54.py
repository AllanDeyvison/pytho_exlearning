print ( 3 * "Allan ")

nome = input ('Seu nome: ')
idade = input('Sua idade: ')
altura = input('Sua altura: ')
peso = input ('Seu peso: ')
imc = int(peso) / (float(altura) ** 2)
ano =2021
nascimento = 2021 - int(idade)

print(nome , 'tem' , idade, 'anos de idade e o imc é', imc)
print(f'{nome} tem {idade} e o imc é { imc:2f}')
print('{} tem {} anos e o imc é {} e o ano de nascimento {}'.format(nome, idade, imc, nascimento))

n1 = int(input('Digite um número: '))
n2 = input('Digite outro número: ')
n2 = int(n2)

print(n1 + n2)