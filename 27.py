def fatorial(x):
    res = 1
    for i in range(1, x + 1):
        res *= i
    return(res)

alunos = int(input('Quantidade de alunos: '))
grupo = int(input('Tamanho de um grupo: '))
outro = int(alunos - grupo)
print(f'Um grupo possui {grupo} membros, logo, o outro possui {outro}.')

a = fatorial(alunos)
b = fatorial(grupo)
c = fatorial(outro)

resultado = a / (b * c)
print(f'É possível fazer {resultado} combinações.')