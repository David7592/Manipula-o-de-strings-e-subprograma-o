censura = ['porra', 'caralho', 'foder', 'filho da puta', 'arrombado']
frase = 'Vai se foder Joãozinho, responde essa porra caralho'

for i in range(len(censura)):
        if censura[i] in frase:
            z = frase.replace(censura[i], censura[i][0] + (len(censura[i]) - 1) * '*')
print(z)