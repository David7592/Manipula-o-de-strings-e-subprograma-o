def quadradomagico(x):
    #linhas
    a = x[0][0] + x[0][1] + x[0][2]
    b = x[1][0] + x[1][1] + x[1][2]
    c = x[2][0] + x[2][1] + x[2][2]
    #colunas
    d = x[0][0] + x[1][0] + x[2][0]
    e = x[0][1] + x[1][1] + x[2][1]
    f = x[0][2] + x[1][2] + x[2][2]
    #diagonalsecundaria
    g = x[2][0] + x[1][1] + x[0][2]
    #diagonalprincipal
    h = x[0][0] + x[1][1] + x[2][2]
    if a == b == c == d == e == f == g == h:
        return('Essa matriz 3x3 é um quadrado mágico.')


matriz = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]

for i in matriz:
    print(i)

print(quadradomagico(matriz))