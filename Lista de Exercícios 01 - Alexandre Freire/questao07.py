lista = []

def inserir(op):
    lista.append(op)

def excluir(num):
    lista.pop(num -1)

def tarConc(num):
    indice = num - 1
    lista[indice] += " - TAREFA REALIZADA"

def listTar():
    for i in range(0, len(lista)):
        print((str(i+1)), "-", lista[i], "\n")

print("+"+42*"-"+"+")
print('|                                          |')
print('|             LISTA DE TAREFAS             |')
print('|                                          |')
print("+"+42*"-"+"+")
print("| 1 - Inserir tarefa                       |")
print("| 2 - Marcar tarefa como concluída         |")
print("| 3 - Excluir tarefa                       |")
print("| 4 - Listar tarefas                       |")
print("| 5 - Sair                                 |")
print("+"+42*"-"+"+")

op = 0

while op != 5:
    op = int( input("Digite sua opção: "))

    if op == 1:
        novTar = input("Nova tarefa: ")
        inserir(novTar)

    if op == 2:
        listTar()
        num = int( input("Qual tarefa deseja marcar como concluída: "))
        tarConc(num)

    elif op == 3:
        listTar()
        num = int( input("Qual tarefa deseja excluir: "))
        excluir(num)

    elif op == 4:
        listTar()

else:
    print("\nSessão encerrada.")