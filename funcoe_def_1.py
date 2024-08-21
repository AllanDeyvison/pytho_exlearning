
def saudacao(msg='Olá', nome='user'):
    nome = nome.replace('e', '3')
    print(msg, nome)

saudacao()
saudacao(nome='Deyvison', msg='Allan')
saudacao('Allan', 'Deyvison')

def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2

divide = divisao(8, 4)

if divisao():
    print(divide)
else:
    print('Invalido')