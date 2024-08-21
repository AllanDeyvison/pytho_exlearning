nome = input("Qual é seu nome? ")
qtd_letras = len(nome)

if qtd_letras <= 4:
    print('Seu nome é curto.')
elif qtd_letras >=5 :
    print('Seu nome é normal')
elif qtd_letras > 6:
    print('Seu nome é muito grande.')