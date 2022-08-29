def splitChars(string):
    upper = ""
    lower = ""
    remainder = ""
    tup = ()

    soma = sum([int(i) for i in string if i.isdigit()])

    for i in string:
        if i not in upper:
            if i >= "A" and i <= "Z":
                upper+=(i)

    for i in string:
        if i not in lower:
            if i >= "a" and i <= "z":
                lower+=(i)

    for i in string:
        if i not in remainder:
            if(ord(i) > 122) or (ord(i) < 48) or (ord(i) > 57 and ord(i) < 65) or (ord(i) > 90 and ord(i) < 97):
                remainder+=(i)

    tup = (soma, upper, lower, remainder)
    return tup

caract = input("Digite algo (letras, números e símbolos): ")
print("Tupla: ", splitChars(caract))