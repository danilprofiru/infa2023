f = open('24.txt')
s = f.readline()
n = []
mx = k = 0
for i in range(len(s)-2):
    if s[i] == s[i+2]:
        n.append(s[i+1])
for j in range(len(n)):
    if n.count(n[j]) > mx:
        mx = n.count(n[j])
        k = n[j]
print(k)
# Считает долго, но верно