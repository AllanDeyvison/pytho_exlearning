
frase = 'o rato roeu a eoupa do rei de roma'

tm_frase = len(frase)
contador = 0
nova_string = ''

input_do_user = input('Qual letra deseja colocar maiúscula: ')

while contador < tm_frase:
    #print(frase[contador], contador)
    #nova_string += frase[contador]
    letra = frase[contador]
    if letra == input_do_user:
        nova_string += input_do_user.upper()
    else:
        nova_string += letra
    contador +=1
    #print(nova_string)

print(nova_string)