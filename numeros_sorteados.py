#Módulos padrão do Python:
#Módulos são arquivos .py ( que contém código python) e servem para expadir
#as funcionalidades padrão da linguagem.
#pip istalll pymysql
import random

numeros_mega = []
numeros_quina = []
numeros_quina2 = []
#
# for i in range(60):
#     n = random.randint(1, 60)
#     if n not in numeros_mega:
#         numeros_mega.append(n)
#
#     if len(numeros_mega) == 6:
#         break
#
# print(numeros_mega)

# def quina2 (quina):
#     for i in range(25):
#         n2 = random.randint(26, 51)
#         if n2 not in numeros_quina2:
#             if n2 not in quina:
#                 numeros_quina2.append(n2)
#         if len(numeros_quina2) == 15:
#             break
# print(f'quina 2: "{numeros_quina2}')

for i in range(25):
    n = random.randint(1, 25)
    if n not in numeros_quina:
        numeros_quina.append(n)
    if len(numeros_quina) == 15:
        break
# quina2(numeros_quina)
print(f'Quina 1: "{numeros_quina}')

