cont = 0
listaPar = []

for i in range(0, 12):
    num = int( input("Digite um número: "))

    if num % 2 == 0:
        listaPar.append(num)
        


print("A média dos números pares é: {:.1f}".format(sum(listaPar)/len(listaPar)))