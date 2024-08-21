# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json 

class People:
    ano = 2024

    def __init__(self, nome, idade):
        
        self.nome = nome
        self.idade = idade
    
    def anoNascimento(self):
        return People.ano - self.idade


pessoa1 = People("allan", 24)
pessoa2 = People("alana", 19)
pessoa3 = People("andreia", 44)

# pessoas =  vars(pessoa1),  vars(pessoa2),  vars(pessoa3)


pessoas ={
    'Pessoa 1': vars(pessoa1),
    'Pessoa 2': vars(pessoa2),
    'Pessoa 3': vars(pessoa3)
}

# print(pessoas)

pessoa1Json = json.dumps(pessoas, indent=True)

arqui = open("classePeople.json", "w").write(pessoa1Json)

# with open('dadosClassePessoa.json', 'w+') as file:
#     file.write(pessoa1Json)
#     file.seek(0)
#     print(file.read())

    