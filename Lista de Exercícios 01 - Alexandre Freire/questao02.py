nome = str( input("Digite o nome do usuário: ")).upper()

esp = " "

for i in range(0, len(nome)+1):
    print(esp, nome[i: len(nome)])
    esp += " "
