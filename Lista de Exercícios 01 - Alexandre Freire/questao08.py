list_A = []
list_B = []

def uniao(list_A, list_B):
    un = []

    for i in range(0, len(list_A)):
        for j in range(0, len(list_B)):
            if list_A[i] == list_B[j]:
                del list_B[j]
                break
    un = list_A + list_B
    return un

def interseccao(list_A, list_B):
    inter = []

    for i in range(0, len(list_A)):
        for j in range(0, len(list_B)):
            if list_A[i] + list_B[j]:
                inter.append(list_A[i])
    return inter

def diferenca(list_A, list_B):
    dif = []

    for i in list_B:
        if i not in list_A:
            dif.append(i)
    return dif

elem1 = int( input("Adicionar o número de elementos da lista 1: "))
for i in range(0, elem1):
    list_A.append( input("Digite os elementos da lista 1: "))

print("\n")

elem2 = int( input("Adicionar o números de elementos da lista 2: "))
for i in range(0, elem2):
    list_B.append( input("Digite os elementos da lista 2: "))

print(f"\nA união das listas: {uniao(list_A, list_B)}")
print(f"\nA intersecção das listas: {interseccao(list_A, list_B)}")
print(f"\nA diferença das listas: {diferenca(list_A, list_B)}")