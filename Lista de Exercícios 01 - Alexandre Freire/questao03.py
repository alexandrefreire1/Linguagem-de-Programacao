matriz = []
tam_mat = 3
lista = []

for i in range(0, tam_mat):
    matriz.append([0]*tam_mat)

for lin in range(0, tam_mat):
    for col in range(0, tam_mat):
        matriz[lin][col] = int( input("Digite um número: "))

for lin in range(0, tam_mat):
    for col in range(0, tam_mat):
        print(matriz[lin][col], end = " ")
        print(" ")

lista.append(matriz[0][2])
lista.append(matriz[1][1:3])
lista.append(matriz[2][0:3])

print("Elementos do triângulo inferior direito da matriz: ", lista)