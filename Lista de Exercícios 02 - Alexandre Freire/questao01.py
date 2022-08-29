# Crie um programa Python que emite “beeps” em uma hora e minuto marcados pelo usuário. 
# Dessa forma, o programa deverá receber do usuário a hora e o minuto que ele quer que 
# o alarme dispare (o beep). Quando chegar na hora e minuto exatos o alarme deverá tocar 5 vezes (5 beeps).

from datetime import datetime
import winsound

print("========================== Alarme ==========================\n")

hora = str( input("Digite a hora para tocar o alarme |hh:mm|: "))
despertador = datetime.strptime(hora, '%H:%M')

print(f"O despertador tocará às {despertador.hour}:{despertador.minute}.\n")
print("============================================================")

while True:
    if datetime.now().hour == despertador.hour and datetime.now().minute == despertador.minute:
        for i in range(5):
            winsound.Beep(500, 1000)
        break