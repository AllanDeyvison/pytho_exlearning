num = input('Digite um número: ')

if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print('Par!')
    else:
        print('Ímpar!')
else:
    print('ERRO')
