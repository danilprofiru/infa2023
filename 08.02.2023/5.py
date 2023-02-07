f = open('zadanie24_2 (1).txt')
s = f.readline()
s = s.replace('R', 'x')
k = mx = 0
for i in range(len(s)):
    if s[i] == 'x':
        k += 1
    else:
        mx = max(k, mx)
        k = 0
print(mx)