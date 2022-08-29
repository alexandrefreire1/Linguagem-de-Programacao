# Faça um programa Python que, através de uma API JSON, obtenha a cotação do dólar e do euro.
# O programa deve receber um valor em reais do teclado e convertê-lo para dólares e euros.
# Como saída, a aplicação deverá apresentar a cotação do dólar e do euro e a conversão dos reais fornecidos como entrada.

import json
import requests

URL = ("http://economia.awesomeapi.com.br/json/all")
resposta = requests.get(URL)
resposta.raise_for_status()

valor = int( input("Digite o valor em reais (BRL) para converter: R$"))
print("\n")

dados = json.loads(resposta.text)

dolarCom = dados['USD']
dolarTur = dados['USDT']
euro = dados['EUR']

print(f"Hora e Data: {dolarCom['create_date']}")
print(f"Cotação do {dolarCom['name']}: ${dolarCom['high']}")
print(f"Cotação do {dolarTur['name']}: ${dolarTur['high']}\n")

print(f"Hora e Data: {euro['create_date']}")
print(f"Cotação do {euro['name']}: €{euro['high']}\n")

print(f"Conversão das moedas: \n")

usd = float(dolarCom['high'])
eur = float(euro['high'])
convUSD = valor / int(usd)
convEUR = valor / int(eur)

print(f"O valor R${valor} reais para o Dólar é: ${convUSD:.2f} dólares.")
print(f"O valor R${valor} reais para o Euro é: €{convEUR:.2f} euros.\n")