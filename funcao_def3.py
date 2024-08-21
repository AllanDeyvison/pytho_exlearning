variavel = 'valor'

def funcao():
    print(variavel)

def funcao2(arg=None):
    #global variavel
    #variavel - 'outro valor'
    #print(variavel)
    arg = arg.replace('v', 'c')
    return arg

funcao()
funcao2()

outra_variavel = funcao2(arg = variavel)
print(variavel)