f = open('24_demo.txt')
s = f.readline()
k = mx = 0
for i in range(len(s)):
    if (s[i] == 'X' and k % 3 == 0) \
            or (s[i] == 'Y' and k % 3 == 1) \
            or (s[i] == 'Z' and k % 3 == 2):
        k += 1
    else:
        mx = max(k, mx)
        k = 0
print(mx)