def determinante(x):
    z = (x[0][0] * x[1][1]) - (x[0][1] * x[1][0])
    return z


matriz = [[2, 4], [1, 3]]

for i in matriz:
    print(i)

print(f'Cálculo da determinante: {determinante(matriz)}')