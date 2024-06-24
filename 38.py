import math
def distancia(x1, x2, y1, y2):
    d = math.sqrt(((y1 - x1)**2 + (y2 - x2)**2))
    return (f'A distância eclidiana é: {d}')


print('***INFORME OS VALORES***')
a1 = float(input('x1: '))
b1 = float(input('y1: '))
a2 = float(input('x2: '))
b2 = float(input('y2: '))
print(distancia(a1, a2, b1, b2))