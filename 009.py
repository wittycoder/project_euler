found = False

for a in range(1, 999):
    if found == True:
        break
    for b in range(a+1, 999):
        if found == True:
            break
        for c in range(b+1, 999):
            if (a**2 + b**2) == c**2:
                if a + b + c == 1000:
                    print(a, b, c)
                    print('=', a * b * c)
                    found = True
                    break
