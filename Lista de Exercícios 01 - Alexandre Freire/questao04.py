dd = input("Data de Nascimento: ")

data = dd.split(" de ")
mm = data[1]
pos = 0

meses = ["Janeiro",
        "Fevereiro",
         "Março",
         "Abril",
         "Maio",
         "Junho",
         "Julho",
         "Agosto",
         "Setembro",
         "Outubro",
         "Novembro",
         "Dezembro"
         ]

for i in range(0, 12):
    if mm == meses[i]:
        pos = i + 1
        break

if pos > 10:
    print(f"Você nasceu em: {data[0]}/{pos}/{data[2]}")

else:
    print(f"Você nasceu em: {data[0]}/{pos}/{data[2]}")
