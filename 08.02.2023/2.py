f = open('17 (2).txt')
s = [int(x) for x in f]
mx = k = 0
for i in range(0, len(s) - 2):
    m = [s[i], s[i + 1], s[i + 2]]
    m.sort()
    if m[2] ** 2 < m[0] ** 2 + m[1] ** 2:
        k += 1
        mx = max(m[0] + m[1] + m[2], mx)
print(k, mx)
