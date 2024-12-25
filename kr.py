def zadacha1():
    a = int(input())
    c = 0
    while a != 0:
        d = a % 10
        if d % 2 !=0:
            c+=d
        a //= 10
    print(c)
def zadacha2():
    a = input()
    if a == a[::-1]:
        print("YES")
    else:
        print("NO")
def zadacha3():
    a = int(input())
    c = []
    for i in range(1, a):
        if a % i == 0:
            c.append(i)
    print(max(c))
def zadacha4():
    a = int(input())
    c = 0
    for i in range(1, a):
        if a % i == 0:
            c += i
    if c==a:
        print("YES")
    else:
        print("NO")
def zadacha5():
    a = int(input())
    b = int(input())
    while b != 0:
        a, b = b, a % b
    print(a)
zadacha1()