def z1():
    n = int(input())
    a = []
    for i in range(n):
        x = int(input())
        a.append(x)
    print(a)
def z2():
    a = []
    for i in range(1,27):
        a.append(chr(96+i)*i)
    print(a)
def z3():
    n = int(input())
    a = []
    for i in range(n):
        x = int(input())** 3
        a.append(x)
    print(a)
def z4():
    n = int(input())
    a = []
    for i in range(1, n+1):
        if n % i == 0:
            a.append(i)
    print(a)
def z5():
    n = int(input())
    a = []
    itog = []

    for i in range(n):
        x = int(input())
        a.append(x)
    for i in range(len(a)):
        try:
            c = a[i] + a[i+1]
            itog.append(c)
        except IndexError:
            c = a[i]

    print(itog)
def z6():
    n = int(input())
    pos = []
    neg = []
    zeros = []

    for i in range(n):
        x = int(input())
        if x > 0:
            pos.append(x)
        if x < 0:
            neg.append(x)
        if x == 0:
            zeros.append(x)
    print(pos)
    print(neg)
    print(zeros)


def z7():
    n = int(input())
    a = []
    for i in range(n):
        x = int(input())
        a.append(x)
    del a[145::2]
    print(a)
def z8():
    n = int(input())
    a = []
    for i in range(n):
        x = input()
        a.extend(x)
    print(a)
def z9():
    x = 1
    a = []
    while x !=0:
        x = int(input())
        if x == 0:
            break
        if x not in a:
            a.append(x)

    print(a)
def z10():
    a = list(map(int, input().split()))
    itog = []
    minitog = []
    for i in range(len(a)):
        if a[i] == 0:
            del a[i]
    for elem in a:
        if elem not in minitog:
            count = 0
            for b in a:
                if b == elem:
                    count += 1
            minitog.append(elem)
            c = [elem, count]
            itog.append(c)
    print(itog)

    


z6()