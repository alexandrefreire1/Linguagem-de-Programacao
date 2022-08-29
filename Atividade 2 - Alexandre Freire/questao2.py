sal = float(input("Digite o salário: R$ "))

salReaj = sal + (sal * 5/100)

if sal < 1045.00:
    print("Seu novo salário é: R${:.2f}".format(salReaj))
else:
    print("Não possui direito a aumento salarial.")
