lista = []
qtdPar = 0
listaImp = []
listaPar = []

for i in range(10):
    num = int( input("Digite um número: "))
    lista.append(num)

for i in range(0, len(lista)):
    if (lista[i] % 2 == 0):
        qtdPar += 1
        listaPar.append(lista[i])

    else:
        listaImp.append(lista[i])


print("\nNúmeros pares: ", listaPar)

print("Quantidade de números pares: ", qtdPar)

print("Números ímpares: ", listaImp)

print("Soma dos números ímpares: ", sum(listaImp))
