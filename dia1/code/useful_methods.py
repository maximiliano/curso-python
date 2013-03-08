lista = [1, 2, 3, 4, 5]
len(lista)
# len funciona em listas, dicionarios, 
# conjuntos, tuplas...

for item in lista:
    if item % 2 != 0:
        continue
    print item

for item in lista:
    if item > 3:
        break
    print item

range(10)
