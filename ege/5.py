for x in range(1, 1000000):
    n = bin(x)[2:]
    n = n + str(n.count('1') % 2)
    n1 = n + str(n.count('1') % 2)
    r = int(n1, 2)
    if r > 97:
        print(r)
        break
