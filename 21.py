import unicodedata

def normalise(frase):
    min = frase.lower()
    x = unicodedata.normalize('NFKD', min)
    x = x.encode('ascii', 'ignore')
    print(f'Frase sem acentos: {x}')


normalise('Lápis BCGBSUs sû Ã')


#perguntar se tem outro jeito