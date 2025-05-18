def z1():
    n = int(input())
    a = [[i for i in range(1, n +1)] for i in range(1, n +1)]
    for elem in a:
        print(elem)
def z2():
    n = int(input())
    a = [[i for i in range(1, k +1)] for k in range(1, n +1)]
    for elem in a:
        print(elem)
def z3():
    n = int(input())
    itog = []
    for i in range(n):
        k = list(map(int, input().split()))
        itog.append(k)
    print(itog)
def z4():
    n = int(input())
    itog = []
    for i in range(n):
        k = list(map(int, input().split()))
        if 0 not in k:
            itog.append(k)
    print(itog)
def z5():
    n = int(input())
    m = int(input())
    a = [[[0] * m] * n]
    for elem in a:
        for lem in elem:
            print(lem)


def z6():
    n = int(input())
    m = int(input())
    itog = []
    now = 1
    for i in range(n):
        r = []
        for j in range(m):
            r.append(now)
            now += 1
        itog.append(r)
    for r in itog:
        print(r)
z6()