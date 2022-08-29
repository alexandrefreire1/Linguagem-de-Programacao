dic = {}
aluno = " "

def media(nomeAluno):
    n1 = dic[nomeAluno][0]
    n2 = dic[nomeAluno][1]
    mediaAluno = (n1 + n2) / 2

    return mediaAluno

while aluno != "":
    if aluno == "":
        print("Nome inválido.")
        break

    else:
        aluno = input("Nome do Aluno: ")
        if aluno != "":
            dic[aluno] = float( input("1ª nota: ")), float( input("2ª nota: "))

        else:
            print("Nome inválido.")
            break

nomeAluno = input("Nome do Aluno que deseja obter a média: ")
print("A média é: ", media(nomeAluno))