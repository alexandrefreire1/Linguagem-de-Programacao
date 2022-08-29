def media(m):
    som = sum(m)
    media = som / 12
    return media

temp = []
acimaMedia = 0

meses = {
    0: "Janeiro",
    1: "Fevereiro",
    2: "Março",
    3: "Abril",
    4: "Maio",
    5: "Junho",
    6: "Julho",
    7: "Agosto",
    8: "Setembro",
    9: "Outubro",
    10: "Novembro",
    11: "Dezembro"
    }

for i in range (0, 11):
    temperaturas = float( input("Digite as temperaturas dos meses: "))
    temp.append(temperaturas)

print("A média anual das temperaturas é: {:.1f}°C".format(media(temp)))

for i in range(0, 11):
    if media(temp) < temp[i]:
        print("A temperatura do mês de", meses[i], "é: ", str(temp[i]), "°C")
