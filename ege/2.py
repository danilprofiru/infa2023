print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((y <= z) and (not((y or w) <= (z and x)))) == 1:
                    print(x,y,z,w)
# zwxy
# 1101
# 0110
# 1100