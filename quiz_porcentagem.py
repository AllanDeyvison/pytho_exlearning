perguntas = {
    'Pergunta 1': {
        'pergunta': 'Qual das características av=baixo é mais importante para você?',
        'respostas': {
            'a': 'Força de vontade e coragem.',
            'b': 'Dinheiro e Poder.',
            'c': 'Honra e Coragem.',
            'd': 'Poder e Respeito.',

        },
    },
    'Pergunta 2': {
        'pergunta': 'Você se importa com religião?',
        'respostas': {
            'a': 'Vou na igreja. Mas não me envolvo muito.',
            'b': 'Não ligo muito para isso.',
            'c': 'Acho importante.',
            'd': 'Acho muito importante, sou até extremista.',

        },
    },
    'Pergunta 3': {
        'pergunta': 'Você se importa com família?',
        'respostas': {
            'a': 'Acho importante, porém não me prendo nos meus antepassados. Quero fazer meu próprio cominho.',
            'b': 'Sim! Principalmente quando é de meu interesse.',
            'c': 'Sim! Família é tudo pra mim.',
            'd': 'Família é importante, porém meus objetivos são mais.',

        },
    },
    'Pergunta 4': {
        'pergunta': 'Qual clima te agrada mais?',
        'respostas': {
            'a': 'Calor.',
            'b': 'Clima ameno.',
            'c': 'Frio.',
            'd': 'Chuva e Frio.',

        },
    },
    'Pergunta 5': {
        'pergunta': 'Você se importa com a vingaça?',
        'respostas': {
            'a': 'Lógico! Tomarei o que é meu!',
            'b': 'Muito! Sempre temos que pagar o que devemos!',
            'c': 'Se for pra limpar minha honra eu me importo sim.',
            'd': 'Me importo. Principalmente quando é pra alcançar o poder.',

        },
    },
    'Pergunta 6': {
        'pergunta': 'Você aceitaria um casamento arranjado?',
        'respostas': {
            'a': 'Se for para agradar minha família, eu aceitria.',
            'b': 'Casaria, se isso me deixasse mais rico.',
            'c': 'Nunca! Só me casaria com alguém que eu realmente amo.',
            'd': 'Casaria, se isso me desse mais notoriedade.',

        },
    },
    'Pergunta 7': {
        'pergunta': 'O que é mais importante na sua opnião?',
        'respostas': {
            'a': 'Ter carisma e determinação.',
            'b': 'Ser visto e invejado.',
            'c': 'Se prepara bem para não sofrer em tempos ruins.',
            'd': 'Ter muitas coisas sob meu comando.',

        },
    },
}

print()
print('Qual das quatro principaiss casas seria a sua em Westeros, faça o teste e descubra!')

targaryen = 0
stark = 0
lannister = 0
baratheon = 0

for pergunta, conteudo in perguntas.items():
    print(f'{pergunta}: {conteudo["pergunta"]}')

    print('')
    for resposta, conteudo_resposta in conteudo['respostas'].items():
        print(f'{resposta}) {conteudo_resposta} ')

    print()
    resposta_user = input('Sua resposta: ')

    if resposta_user == 'a':
        targaryen = targaryen + 1
    if resposta_user == 'b':
        lannister = lannister + 1
    if resposta_user == 'c':
        stark = stark + 1
    if resposta_user == 'd':
        baratheon = baratheon + 1

quantidade_pergunta = len(perguntas)

porcentagem_targaryen = targaryen / quantidade_pergunta * 100
porcentagem_lannister = lannister / quantidade_pergunta * 100
porcentagem_stark = stark / quantidade_pergunta * 100
porcentagem_baratheon = baratheon / quantidade_pergunta * 100

print(f'Você é {porcentagem_targaryen}% casa Targaryen')
print(f'Você é {porcentagem_lannister}% casa Lannister')
print(f'Você é {porcentagem_stark}% casa Stark')
print(f'Você é {porcentagem_baratheon}% casa Baratheon')


