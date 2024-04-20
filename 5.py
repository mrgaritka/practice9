def pal5(x):
    x1 = x // 10000
    x2 = (x // 1000) % 10
    x3 = (x // 100) % 10
    x4 = (x // 10) % 10
    x5 = x% 10
    if x1 == x5 and x2 == x4:
        return 1

def pal4(x):
    x1 = x // 1000
    x2 = (x // 100) % 10
    x3 = (x // 10) % 10
    x4 = x% 10
    if x1 == x4 and x2 == x3:
        return 1

def pal6(x):
    x1 = x // 100000
    x2 = (x // 10000) % 10
    x3 = (x // 1000) % 10
    x4 = (x // 100) % 10
    x5 = (x // 10) % 10
    x6 = x % 10
    if x1 == x6 and x2 == x5 and x3 == x4:
        return 1

for i in range(9999, 999999+1):
    if (pal5(int(str(i)[1:])) == 1 and pal5(int(str(i+1)[1:])) == 1 and pal4(int(str(i+2)[1:4])) == 1
            and pal6(i+3) == 1):
        print(i)
        break