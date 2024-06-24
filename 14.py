def linha(z):
    print(z)


l = '-----------------'
linha(l)
print('Digite o telefone')
linha(l)

def num(x, y):
    if range(len(x)) == range(len(y)):
        print('Telefone:', x + '-' + y)
    elif range(len(x)) != range(len(y)):
        print('Telefone com 7 dígitos, o 3 será acrescentado na frente.')
        print('Telefone:', '3' + x + '-' + y)


num1, num2 = input('quatro primeiros: '), input('consecutivos: ')
num(num1, num2)