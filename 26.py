print('------------------\n(1)Circunferência\n(2)Triângulo\n(3)Retângulo\n------------------')
x = int(input('Escolha (1, 2 ou 3): '))

if x == 1:
    r = float(input('Valor do raio: '))
    perimetro = 2 * 3.14 * r
    print(perimetro)
elif x == 2:
    l1 = float(input('Valor do lado 1: '))
    l2 = float(input('Valor do lado 2: '))
    l3 = float(input('Valor do lado 3: '))
    print(l1 + l2 + l3)
elif x == 3:
    b = float(input('Valor da base: '))
    a = float(input('Valor da altura: '))
    p = 2 * (b + a)
    print(p)