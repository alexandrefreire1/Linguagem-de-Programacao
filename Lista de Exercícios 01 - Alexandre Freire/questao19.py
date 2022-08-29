def elimRepet(inteiro):
    listInt = []
    for i in inteiro:
        if i not in listInt:
            listInt.append(i)
    
    return listInt

dig = []

num = int( input("Quantidade de números na lista: "))

for i in range(0, num):
    dig.append(int( input("Digite um número: ")))

else:
    print("\n")
    print("Lista digitada: ", dig)
    print("Lista sem números repetidos: ", elimRepet(dig))