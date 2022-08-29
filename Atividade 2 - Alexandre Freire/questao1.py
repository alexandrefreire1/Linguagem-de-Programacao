ano = int(input("Digite um ano: "))

if (ano % 100 != 0) and (ano % 4 == 0) or (ano % 400 == 0):
    print("Ano bissexto")
else:
    print("Não é um ano bissexto.")
