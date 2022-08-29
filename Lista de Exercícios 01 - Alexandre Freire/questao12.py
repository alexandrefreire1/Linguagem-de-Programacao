def numPrimo(n):
    prim = ""

    for i in range(2, n+1):
        cont = 0
        for j in range(2, i+1):
            if i % j == 0:
                cont += 1
        if cont <= 1:
            prim = prim + " " + str(i)

    return prim

n = int( input("Digite um número: "))

if n >= 2:
    print("Primos:", (numPrimo(n)))
else:
    print("Inválido.")