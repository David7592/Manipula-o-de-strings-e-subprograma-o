def ordenar(lista):
    lista2 = []
    for i in range(max(lista)):
        i += 1
        if i in lista:
            lista2.append(i)
    return(lista2)

num = [1, 6, 3, 9, 2]
print(ordenar(num))