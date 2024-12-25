def zadacha():
    a = int(input())
    c = 0
    while a != 0:
        x = a % 10
        if x % 2 == 0:
            c += 1
        a //= 10
    print(c)
def zadacha2():
    a = int(input())
    b = 0
    for i in range(1, a+1):
        if a % i == 0:
            b+=1
    if a != 1 and b == 2:
        print("YES")
    else:
        print("NO")
def zadacha3():
    a = int(input())
    b = int(input())
    while b != 0:
        a, b = b, a % b
    print(a)
def zadacha4():
    a = input()
    if a == a[::-1]:
        print("YES")
    else:
        print("NO")
def zadacha5():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    sps = []
    for i in range(1, n +1):
        if i % a == 0 and i % b == 0 and i % c == 0:
            sps.append(i)
    print(max(sps))
def zadacha6():
    n = int(input())
    gotovo = []
    for i in range(1,n+1):
        cps = []
        for j in range(1, i+1):
            if i % j == 0:
                cps.append(j)

        if sum(cps) == 2 * i:
            gotovo.append(i)
        cps.clear()
    for elem in gotovo:
        print(elem,end= " ")

def zadacha7():
    prostie = [2,3,5,7]
    n = int(input())
    itog = []
    for i in range(1 , n+1):
        istog = False
        c = []
        d = i
        while d != 0 :
            x = d % 10
            c.append(x)
            d //= 10
        for elem in c:
            if elem != 2 and elem != 3 and elem != 5 and elem !=7:
                isitog = False
                break
            else:
                isitog = True
        if istog:
            itog.append(i)
    for elem in itog:
        print(elem, end=" ")

zadacha6()