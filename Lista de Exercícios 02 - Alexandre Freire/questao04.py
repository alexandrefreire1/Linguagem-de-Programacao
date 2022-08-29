# Utilizando uma API JSON e o módulo Matplotlib, desenvolva uma aplicação que recupera
# os dados da COVID-19 no Brasil e apresenta sua evolução em gráficos.
# Apresente um gráfico geral do Brasil, juntamente com os dados dos contaminados e mortos
# e também permita que o usuário possa escolher algum estado brasileiro que ele deseja ver o gráfico e os dados.

import requests
import json
import os
import matplotlib.pyplot as grafico

URL = "https://api.apify.com/v2/datasets/3S2T1ZBxB9zhRJTBB/items?format=json&clean=1"
resposta = requests.get(URL)
resposta.raise_for_status
dados = json.loads(resposta.text)

def clear():
    import os
    os.system("cls" if os.name == "nt" else "clear")

UF = " "
print("+==========================================================================+")
print("|                      Gráficos da COVID-19 no Brasil                      |")
print("+==========================================================================+\n")
UFs = {
    "Acre": "AC",
    "Alagoas": "AL",
    "Amapá": "AP",
    "Amazonas": 'AM',
    "Bahia": "BA",
    "Ceará": "CE",
    "Distrito Federal": "DF",
    "Espírito Santo": "ES",
    "Goiás": "GO",
    "Maranhão": "MA",
    "Mato Grosso": "MT",
    "Mato Grosso do Sul": "MS",
    "Minas Gerais:": "MG",
    "Pará": "PA",
    "Paraíba": "PB",
    "Pernambuco": "PE",
    "Piauí": "PI",
    "Rio de Janeiro": "RJ",
    "Rio Grande do Norte": "RN",
    "Rio Grande do Sul": "RS",
    "Rondônia": "RO",
    "Roraima": "RR",
    "Santa Catarina": "SC",
    "São Paulo": "SP",
    "Sergipe": "SE",
    "Tocantins": "TO"
}

# Programa recebe Estado do usuário:

estado = input("Digite o nome do estado e veja os dados referentes à COVID-19: ")
for i in range(0, len(UFs)):
    if estado in UFs:
        UF = UFs[estado]
    else:
        print("Estado não existe.")
        break

print(f"\nDados do Estado do/de {estado} ")

# List. e Var. para Dados dos Estados (UFs):

infectEst = []
infectDiasEst = []
mortesEst = []
mortesDiasEst = []
quantInfectEst = 0
quantInfectDiasEst = 0
quantMortesEst = 0
quantMortesDiasEst = 0

# Infectados por Estado:

for i in range(0, 508):
    for j in range(0, len(dados[i]["infectedByRegion"])):
        if dados[i]["infectedByRegion"][j]["state"] == UF:
            quantInfectEst = dados[i]["infectedByRegion"][j]["count"]
            infectEst.append(quantInfectEst)
            quantInfectDiasEst = quantInfectDiasEst + 1
            infectDiasEst.append(quantInfectDiasEst)
        else:
            continue

# Gráfico de Infectados por Estado:

print("Gerando gráfico, aguarde.")
print(" ")
grafico.plot(infectDiasEst, infectEst)
grafico.title(f"Dados do Nº de Casos Confirmados no/em {estado}")
grafico.xlabel("Quant. de Dias da Pandemia")
grafico.ylabel("Quant. de Casos Confirmados")
grafico.show()

# Mortes por Estado:

for i in range(1, 509):
    for j in range(0, len(dados[i]["deceasedByRegion"])):
        if dados[i]["deceasedByRegion"][j]["state"] == UF:
            quantMortesEst = dados[i]["deceasedByRegion"][j]["count"]
            mortesEst.append(quantMortesDiasEst)
            quantMortesDiasEst = quantMortesDiasEst + 1
            mortesDiasEst.append(quantMortesDiasEst)
        else:
            continue

# Gráfico de Mortes por Estado:

grafico.plot(mortesDiasEst, mortesEst)
grafico.title(f"Dados do Nº de Mortos no/em {estado}")
grafico.xlabel("Quant. de Dias da Pandemia")
grafico.ylabel("Quant. de Mortes")
grafico.show()

# List. e Var. de Dados do Brasil:

infectBR = []
mortesBR = []
infectDiasBR = []
mortesDiasBR = []
quantInfectBR = 0
quantMortesBR = 0
quantInfectDiasBR = 0
quantMortesDiasBR = 0

# Infectados no Brasil:

for i in range(0, 509):
    quantInfectBR = dados[i]["infected"]
    infectBR.append(quantInfectBR)
    quantInfectDiasBR = quantInfectDiasBR + 1
    infectDiasBR.append(quantInfectDiasBR)

# Gráfico dos Infectados no Brasil:

grafico.plot(infectDiasBR, infectBR)
grafico.title(f"Dados do Nº de Casos Confirmados no Brasil")
grafico.xlabel("Quant. de Dias da Pandemia")
grafico.ylabel("Quant. de Casos Confirmados (em milhões)")
grafico.show()

# Mortes no Brasil:

for i in range(0, 509):
    quantMortesBR = dados[i]["deceased"]
    mortesBR.append(quantMortesBR)
    quantMortesDiasBR = quantMortesDiasBR + 1
    mortesDiasBR.append(quantMortesDiasBR)

# Gráfico da quant. de Mortes no Brasil:

grafico.plot(mortesDiasBR, mortesBR)
grafico.title(f"Quantidade de Mortes no Brasil")
grafico.xlabel("Quant. de Dias da Pandemia")
grafico.ylabel("Quant. de mortos")
grafico.show()

# Resultado gerados dados da COVID-19 no país:

print("+==========================================================================+")
print("|                     Dados gerais do Estado escolhido                     |")
print("+==========================================================================+")
print(f"   Total de Casos Confirmados no/em {estado}: {infectEst[-1]}              ")
print(f"   Total de Mortes no/em {estado}: {mortesDiasEst[-1]}                     ")
print("+==========================================================================+")
print("\n")
print("+==========================================================================+")
print("|                          Dados gerais do Brasil                          |")
print("+==========================================================================+")
print(f"   Total de Casos Confirmados no país: {infectBR[-1]}                      ")
print(f"   Total de Mortes no país: {mortesBR[-1]}                                 ")
print(f"   Quantidade de dias da Pandemia: {quantInfectDiasBR}                     ")
print("+==========================================================================+")