k = 0
alf = 'ABCDEX'
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                s = x1 + x2 + x3 + x4
                if s.count('X') == 1:
                    if x1 == 'X':
                        k += 1
                    elif x4 == 'X':
                        k += 1
print(k)