
def funcao(num1, num2):
    porcentagem = num1*(num2/100)
    num1 = porcentagem + num1
    return num1

numero = input('Digite um número:')
porce = input('Digite quantos %:')
numero = int(numero)
porce = int(porce)

print(funcao(numero, porce))

