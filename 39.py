'''pesquisei sobre o Merge Sort e vi que ele é basicamente a função .sort em uma lista, mas ele é feito por
meio de um método de divisão super eficiente. Porém, eu não dei conta de fazer.'''

def mergesort(x):
    x.sort()
    return x


lista = [1, 4, 2, 3, 9, 43, 22, 10]
print(mergesort(lista))