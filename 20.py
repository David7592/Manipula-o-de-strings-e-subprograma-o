def certo(email):
    if '.com' not in email:
        print('Falta o ".com".')
    elif '@' not in email:
        print('Falta o "@".')
    else:
        print(f'Seu email: {email}')


certo('15dca15@gmail.com')