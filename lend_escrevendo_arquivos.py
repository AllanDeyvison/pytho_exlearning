import json

d1 ={
    'Pessoa 1':{
        'nome': 'Allan',
        'idade': 21
    },
    'Pessoa 2':{
        'nome': 'Deyvison',
        'idade': 22
    },
}

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)






with open('abc.txt', 'w+') as file:
    file.write('linha 1\n')
    file.write('linha 2\n')
    file.write('linha 3\n')
    file.write('linha 4\n')

    file.seek(0)
    print(file.read())

"""
file = open('abc.txt', 'w+')
file.write('linha 1\n')
file.write('linha 2\n')
file.write('linha 3\n')

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print('____________________________')

file.seek(0,0)
for linha in file:
    print(linha, end='')

file.close()
"""