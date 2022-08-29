buscaResult = []
plvrs = []

def proc(string):
    i = 0
    tam = len(string)

    while i < len(plvrs):
        if string == plvrs[i][0:tam]:
            buscaResult.append(plvrs[i])
        i += 1

    return buscaResult

numPlvrs = int( input("Número de palavras na lista: "))

for i in range(0, numPlvrs):
    add = input("Digite a palavra desejada: ")
    plvrs.append(add)

buscar = input("Digite a palavra que deseja procurar: ")

print(proc(buscar))