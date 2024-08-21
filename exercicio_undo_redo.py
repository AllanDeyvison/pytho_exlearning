"""

nova_tarefa = input('Digite uma nova tarefa: ')
tarefas = []
tarefas.append(nova_tarefa)
print(tarefas)
continuar = input('Quer adicionar uma nova tarefa? ')

while continuar == 's':
    nova_tarefa = input('Digite uma nova tarefa: ')
    tarefas.append(nova_tarefa)
    print(tarefas)
    continuar = input('Quer adicionar uma nova tarefa? ')



print(tarefas)
"""

def tarefa(tarefa, lista_tarefas=None):
    if lista_tarefas is None:
        lista_tarefas = []
    lista_tarefas.extend(tarefa)
    return lista_tarefas

nova_tarefa = input('Digite uma nova tarefa: ')

tarefas_adicionadas = tarefa([nova_tarefa])

print(tarefas_adicionadas)

continuar = input('Quer adicionar uma nova tarefa? ')

while continuar == 's':
    nova_tarefa = input('Digite uma nova tarefa: ')
    tarefas_adicionadas = tarefa([nova_tarefa])

    print(tarefas_adicionadas)
    continuar = input('Quer adicionar uma nova tarefa? ')