from itertools import groupby, tee

alunos = [
    {'nome': 'Allan', 'nota': 'A'},
    {'nome': 'Allana', 'nota': 'B'},
    {'nome': 'Deyvison', 'nota': 'C'},
    {'nome': 'Agatha', 'nota': 'D'},
    {'nome': 'Cersei', 'nota': 'D'},
    {'nome': 'Bianca', 'nota': 'C'},
    {'nome': 'Andreia', 'nota': 'B'},
    {'nome': 'Delon', 'nota': 'B'},
    {'nome': 'Luisa', 'nota': 'A'},
]

ordena = lambda i: i['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)
#alunos.sort(key=lambda i: i['nota'])
#alunos_agrupados = groupby(alunos, lambda i: i['nota'])

for agrupados, valores in alunos_agrupados:
    va1, va2 = tee(valores)

    print(f'Agrupamento: {agrupados}')

    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram nota {agrupados}')
    print()


