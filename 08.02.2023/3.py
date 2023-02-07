f = open('17 (3).txt')
s = [int(x) for x in f]
mx = k = 0
for i in range(0, len(s)-1):
    for j in range(i+1, len(s)):
        if s[i] * s[j] % 10 == 0:
            k += 1
            mx = max(s[i] + s[j], mx)
print(k,mx)