def media(nota):
    if nota >= 6:
        return 'Aprovado'
    if 4 <= nota < 6:
        return 'Verificação suplementar'
    if nota < 4:
        return 'Reprovado'


x = float(input('Média final: '))
print(media(x))