def compressao(texto):
    contador = 0
    res = ''
    for i in range(1, len(texto)):
        if texto[i] == texto[i - 1]:
            contador += 1
        else:
            res += texto[i - 1] + str(contador)
            contador = 1
    res += texto[-1] + str(contador)

    return res


x = 'aaaabbccc'
print(compressao(x))