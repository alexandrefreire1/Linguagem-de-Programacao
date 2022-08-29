from operator import itemgetter

dic = {}
pilotos = []

def melhorVolta():

    menTemp = dic[(pilotos[0])][0]
    volta = 0
    piloto = pilotos[0]

    for corredores in range(0, 6):
        for voltas in range(0, 3):

            if dic[(pilotos[corredores])][voltas] < menTemp:
                menor = dic[pilotos[piloto]][voltas]
                piloto = pilotos[corredores]
                volta = voltas

    print("\nA melhor volta foi a do piloto" + piloto + " na volta ", (volta + 1), " no tempo de: " + str(menTemp))

def classif():
    classific = {}

    for i in range(0, 6):
        classific[pilotos[i]] = int( sum(dic[pilotos[i]]) / 3)

    classific = sorted(classific.items(), key=itemgetter(1))

    print("\nClassificação - Resultado Final\n")

    for i in range(0, 6):
        print(str(i + 1)+"º Lugar", classific[i])

for i in range(0, 6):
    nomPil = input("Nome do piloto " + str(i + 1) + ": ")
    pilotos.append(nomPil)

print("\n")

for i in range(0, 6):
    dic[pilotos[i]] = float( input("Tempo das 3 voltas do piloto " + pilotos[i] + ":\n1ª volta: ")), float( input("2ª volta: ")), float( input("3ª volta: "))
    
melhorVolta()
classif()