num1 = input('Digite um númeor: ')
num2 = input('Digite um númeor: ')

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print ('ERROR')