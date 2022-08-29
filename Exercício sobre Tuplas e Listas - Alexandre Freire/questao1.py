tupla1 = (4, 5, 6)
tupla2 = (11, 12, 13)

tupla3 = [*sum(zip(tupla1, tupla2), ())]

print(tupla3)
