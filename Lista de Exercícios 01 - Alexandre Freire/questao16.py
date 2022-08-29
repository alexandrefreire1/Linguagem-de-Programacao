pos = []
invFras = []

def invOrdem(frase):
    ext = 0
    tam = len(frase) - 1

    for i in range(0, tam):
        if frase[i] == " ":
            pos.append(i)
    pos.append(tam + 1)

    for i in range(0, len(pos)):
        inv = frase[ext: (pos[i])]
        invFras.append(inv)
        ext += (len(inv))+1

    for i in range((len(invFras)-1), -1,-1):
        print(invFras[i], end=" ")

frase = input("Digite a frase: ")
invOrdem(frase)