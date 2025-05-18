from torch.distributions import chi2


def z1():
    n, m = int(input()), int(input())
    itog = []
    maxIs  = []
    for i in range(n):
        k = []
        lowest = 0
        maxIndex = 0
        for j in range(m):
            x = int(input())
            if x > lowest:
                maxIndex = j
                lowest = x
            k.append(x)
        itog.append(k)
        maxIs.append([max(k), i, maxIndex])
    i = []
    for elem in maxIs:
        i.append(elem[0])
    maxCh = max(i)
    for elem in maxIs:
        if elem[0] == maxCh:
            print(elem[1], elem[2])
            break
    print(itog)
def z2():
    n = int(input())
    itog  = []
    for i in range(n):
        x = list(map(int, input().split()))
        itog.append(x)
    print(itog)
    ch1 = []
    ch2 = []
    for i in range(n):
        for j in range(n):
            if (i < j and i < n - 1 - j) or (j > i > n - 1 - j):
                ch1.append(itog[i][j])
            if j < i < n - 1 -j  or (i > j and i > n - 1 -j):
                ch2.append(itog[i][j])
    if ch1 == ch2:
        print(True)
    else:
        print(False)
def z3():
    n = int(input())
    itog = []
    for i in range(n):
        k = list(map(int, input().split()))
        itog.append(k)
    sumka = 0
    for i in range(n):
        for j in range(n):
                sumka += itog[i][i]
    print(sumka)
def z4():
    n, m = int(i)
z2()
# 1 2 3 4
# 4 1 3 4
# 4 3 1 4
# 4 3 2 1
