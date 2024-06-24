def frase(a, antiga, nova):
    frase2 = ''
    for i in a:
        frase2 += i
        frase3 = frase2.replace(antiga, nova)
    print(f'Fase antiga: {a}\nFrase nova: {frase3}')


x = input('Escolha uma string pra alterar: ')
y = input('Nova string: ')
frase('Quem parte e reparte fica com a maior parte.', x, y)