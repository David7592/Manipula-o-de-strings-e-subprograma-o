def contar(frase):
    palavras = frase.split()
    lista = {}

    for i in palavras:
        if i in lista:
            lista[i] += 1
        else:
            lista[i] = 1
    return lista


string = 'Em noites de Lua cheia, os peixes sobem até a superfície.'
print(contar(string))