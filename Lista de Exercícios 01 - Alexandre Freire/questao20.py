lista = []

def montarChar(string):
    cont = 0

    for i in range(0, len(string)):
        for j in range(0, len(lista)):

            if string[i] == lista[j]:
                del lista[j]
                cont+=1
                break

    return cont == len(string)

num = int( input("Quantidade de letras na lista: "))

for i in range(0, num):
    letras = input("Digite as letras da lista: ")

    if len(letras) == 1:
        lista.append(letras)
    else:
        print("Uma letra por seção.")
        i-=1

plvr = input("Digite a palavra que quer obter: ")
print(montarChar(plvr))