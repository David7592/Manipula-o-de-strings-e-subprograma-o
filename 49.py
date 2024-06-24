def semintervalo(string):
    res = []
    i = 0

    while i < len(string):
        x = 0
        while i < len(string) and string[i].isdigit():
            x = x * 10 + int(string[i])
            i += 1
        if i < len(string) and string[i] == '-':
            i += 1
            end = 0
            while i < len(string) and string[i].isdigit():
                end = end * 10 + int(string[i])
                i += 1
            num = x
            while num <= end:
                res.append(num)
                num += 1
        else:
            res.append(x)
        if i < len(string) and string[i] == ',':
            i += 1
    return res


num = "1-3,5,7-9"
print(f"Intervalos: {num}")
print(f"Em intervalos: {semintervalo(num)}")