def verifica(texto):
    for i in texto:
        if i == '(':
            if ')' not in texto:
                return (f'Parênteses imcompleto, verifique o texto: "{texto}"')
        elif i == '[':
            if ']' not in texto:
                return (f'Colchetes imcompleto, verifique o texto: "{texto}"')
        elif i == '{':
            if '}' not in texto:
                return (f'Chaves imcompleto, verifique o texto: "{texto}"')
            

string = '{A}ma[nã é segu(nd)a.'
print(verifica(string))