def dna(entrada):
    dna2 = ''
    for i in entrada:
        if i == 'A':
            dna2 += 'T'
        elif i == 'T':
            dna2 += 'A'
        elif i == 'G':
            dna2 += 'C'
        elif i == 'C':
            dna2 += 'G'
    print(dna2)


x = input('Cadeia de DNA: ')
dna(x)