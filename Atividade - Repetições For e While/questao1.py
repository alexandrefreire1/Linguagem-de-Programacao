cont = 0

for i in range(0, 10):
    idade = int( input("Digite a idade: "))
    
    if idade >= 18:
        cont +=1

print("A quantidade de pesoas maiores de idade é: ", cont)