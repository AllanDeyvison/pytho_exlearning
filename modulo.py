#Módulos padrão do Python:
#Módulos são arquivos .py ( que contém código python) e servem para expadir
#as funcionalidades padrão da linguagem.
#pip istalll pymysql
import random

numeros_sortiados =[]

seis = 60

for i in range(60):
    n = random.randint(1, 6)
    if n not in numeros_sortiados:
        numeros_sortiados.append(n)

    if len(numeros_sortiados) == 6:
        break

print(numeros_sortiados)



