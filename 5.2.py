for x in range(1, 100000):
    n = x
    s = ""
    while n > 0:
        s += str(n % 3)
        n //= 3
    s = str(x % 3) + s
    r = 0
    for i in range(len(s)):
        r += int(s[i]) * 3 ** i
        c = str(r)
    if len(c) >= 4:
        print(c)
        break