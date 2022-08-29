posNome = {}
posNome2 = {}
lista = {}
i = 0
num = []

def incNome(nome, numero):
    if op == 1:
        pos = posNome[nome]
        lista[nome] = num[pos]

def incTel(nome, numero):
    pos = posNome[nome]
    lista[nome] = num[pos]

def excTel(nome, numero):
    del lista[nome][numero]

def excNome(nome):
    del lista[nome]
    del posNome2[posNome[nome]]
    del posNome[nome]

def mostre(op):

    print('\n')
    print('+'+31*'-'+'+')
    print('|       Lista de Contatos       |')
    print('+'+31*'-'+'+')
        
    print(lista)

print('+'+43*'-'+'+')
print('|                                           |')
print('|           AGENDA TELEFÔNICA               |')
print('|                                           |')
print('+'+43*'-'+'+')
print('| 1 - INCLUIR NOVO NOME                     |')
print('| 2 - INCLUIR TELEFONE                      |')
print('| 3 - EXCLUIR TELEFONE                      |')
print('| 4 - EXCLUIR NOME                          |')
print('| 5 - CONSULTAR TELEFONE                    |')
print('+'+43*'-'+'+')

op = -1

while op != 6:
    op = int( input("Digite a opção desejada: "))
    if op == 1:
        nome = input("Digite o nome do contato: ")
        numero = int( input("Digite o número: "))
        posNome[nome] = i
        posNome2[i] = nome
        n = [numero]
        num.append(n)
        
        inserir(nome, numero)

        i+=1

    elif op == 2:
        nome = input("Deseja adicionar um número a que contato? ")
        nvNum = int( input("Digite o novo número: "))

        pos = posNome[nome]
        num[pos].append(nvNum)
        
        inserir(nome, nvNum)

    elif op == 3:
        mostre(op)
        nome = input("Digite a opção a ser excluída: ")
        excNum = int( input("Digite a posição do número para excluir: "))
        excNum = excNum - 1
        excTel(nome, excNum)

    elif op == 4:
        mostre(op)
        nome = input("Digite o contato que quer excluir: ")
        excNome(nome)

    elif op == 5:
        mostre(op)

else:
    print("\nFim da sessão.")