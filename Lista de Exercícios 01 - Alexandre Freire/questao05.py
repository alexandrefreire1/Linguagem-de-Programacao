import random

palavras = ["Microsoft", "Apple", "Samsung", "iPhone", "MacOS", "Mouse", "Placa de Vídeo", "Notebook", "Desktop"]

correta = random.choice(palavras)

list(correta)

a = (correta[0:2])
b = (correta[3:4])
c = (correta[4:7])
d = (correta[2:3])
e = (correta[7:])

print("Início de Jogo! A palavra é:", end = " ")
print(e, end = " ")
print(a, end = " ")
print(c, end = " ")
print(d, end = " ")
print(b, end = " ")

print("\n")

cont = 0

for i in range(0, 3):
    digite = str( input("Digite a palavra correta: "))

    if digite == correta:
        cont += 1
        break

    else:
        print("Você errou, tente novamente.")

print("\n")

if cont != 0:
    print("Parabéns! Você ganhou o jogo!")
    print("A palavra certa é:", correta)

else:
    print("Você perdeu o jogo.")
    print("A palavra correta é:", correta)
