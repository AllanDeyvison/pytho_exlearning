while True:
    print()
    sair = input(' Continuar [s]in ou [n]ão: ')
    num_1 = input('Número: ')
    num_2 = input('Nùmero: ')
    operador = input('Operador: ')
    if sair == 's':
        break

    if not  num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        continue
    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print('Operador invalido.')