listPlvr = []
inv = []

def invRetira(listPlvr, padrao):

    for i in range(0, len(listPlvr)):
        plvrs = ""
        for j in range(0, len(listPlvr[i])):

            if listPlvr[i] != padrao:
                if listPlvr[i][j] == listPlvr[i][j].upper():
                    plvrs += (listPlvr[i][j].lower())

                else:
                    plvrs += (listPlvr[i][j].upper())
        inv.append(plvrs)

    for i in range((len(inv)-1), -1,-1):
        print(inv[i], end = " ")
    
num = int( input("Quantidade de itens da lista: "))

for i in range(0, num):
    plvr = input("Digite uma palavra: ")
    listPlvr.append(plvr)

padrao = input("Digite a palavra padrão: ")

print("\n")

invRetira(listPlvr, padrao)