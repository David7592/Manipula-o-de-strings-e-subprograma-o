def organiza(nome):
    for i in range(len(nome)):
        x = nome.upper()
        print(x[i])

x = input('Inserir nome: ')
organiza(x)