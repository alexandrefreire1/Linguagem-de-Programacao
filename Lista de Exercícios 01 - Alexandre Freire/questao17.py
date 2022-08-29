def digExt(num):
    maiNum = 0
    menNum = num % 10
    tupla = ()

    while num > 0:
        a = num % 10
        if a > maiNum:
            maiNum = a
        if a < menNum:
            menNum = a
        num = num // 10

    tupla = (menNum, maiNum)
    print(tupla)

num = int( input("Digite um número de mais de dois dígitos positivos: "))

if num > 99:
    (digExt(num))

else:
    print("Digite um número válido!")