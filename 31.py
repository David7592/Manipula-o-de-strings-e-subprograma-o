def fibonacci(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    a, b = 0, 1
    for _ in range(num - 2):
        a, b = b, a + b
    return b


x = int(input('Número: '))
print(f'O {x}-ésimo número da sequência é: {fibonacci(x)}')