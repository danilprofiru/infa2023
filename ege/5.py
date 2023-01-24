for x in range(1, 100000):
    n = bin(x)[2:]
    n += n[-1]
    if n.count('1') % 2 == 0:
        n += '0'
    else: n += '1'
    if n.count('1') % 2 != 0:
        n += '1'
    r = int(n, 2)
    if r > 105:
        print(r)
        break

#Ответ 111