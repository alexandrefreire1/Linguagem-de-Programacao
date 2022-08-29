listaAlt = []

idade = int( input("Digite a idade: "))
alt = float( input("Digite a altura: "))

if (idade > 50):
    listaAlt.append(alt)

while idade > 0:
    idade = int( input("Digite a idade: "))
    alt = float( input("Digite a altura: "))

    if idade > 50:
        listaAlt.append(alt)

    elif idade <= 0:
        print("A média das alturas dos indivíduos com mais de 50 anos é: {:.2f}".format(sum(listaAlt) / len(listaAlt)))
