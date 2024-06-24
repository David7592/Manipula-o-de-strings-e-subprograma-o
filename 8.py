def escada(nome):
    maiusculo = nome.upper()
    for i in range(1, len(maiusculo) + 1):
        print(maiusculo[:i])


entrada = input('Insira um nome: ')
escada(entrada)