def completo(frase, matriz):
    frase1 = frase.lower()
    for i, j in matriz:
        frase1 = frase1.replace(i.lower(), j.lower())
    return frase1


matriz = [['vc', 'você'], ['q', 'que'], ['tbm', 'também']]
string = 'vc tem q vir aqui tbm.'
print(completo(string, matriz))