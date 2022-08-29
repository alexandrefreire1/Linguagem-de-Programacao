peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

if imc < 20:
    print("Abaixo do peso.")
elif (imc >= 20) and (imc <= 25):
    print("Peso normal.")
elif (imc >= 25) and (imc <= 30):
    print("Acima do peso.")
else:
    print("Obesidade.")

print("Seu IMC é: {:.2f}".format(imc))
