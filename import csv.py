import csv
import copy
import re

with open ('preproinsulin-seq.txt') as file:
    fileString = file.read() .replace(" ", "")
    fileString2 = fileString.strip("1/ORGIN")
    print(fileString2)
    print("______________")
    print(fileString)


    import re

# Abre o arquivo e lê todas as linhas
with open('preproinsulin-seq.txt', 'r') as originalFile:
  lines = originalFile.readlines()
  pass

# Remove a primeira e última linha
del lines[0]
del lines[-1]

# Para as linhas que sobraram, remove todos os números e espaços em branco
lines[0] = re.sub(r'[\d\s]', '', lines[0])
lines[1] = re.sub(r'[\d\s]', '', lines[1])


# Escreve as linhas modificadas para um novo arquivo
with open('preproinsulin-seq-clean.txt', 'w') as regexFile:
  regexFile.writelines(lines)
  pass

with open('preproinsulin-seq-clean.txt', 'r') as filtros:
  textoFull = filtros.readlines()
  pass

conteudo = ''.join(textoFull)

primeiraParte = conteudo[:24]
segundaParte = conteudo[24:54]
terceiraParte = conteudo[54:89]
quartaParte = conteudo[89:110]

with open('lsinsulin-seq-clean.txt', 'w') as primeiroFiltro:
  primeiroFiltro.write(primeiraParte)
  pass

with open('binsulin-seq-clean.txt', 'w') as segundoFiltro:
  segundoFiltro.write(segundaParte)
  pass

with open('cinsulin-seq-clean.txt', 'w') as terceiroFiltro:
  terceiroFiltro.write(terceiraParte)
  pass

with open('ainsulin-seq-clean.txt', 'w') as quartoFiltro:
  quartoFiltro.write(quartaParte)
  pass