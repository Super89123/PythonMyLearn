from operator import truediv


def z1():
    a = [12, 43, 231]
    a.insert(2, 100)
    print(a)
def z2():
    a = list(map(str, input().split(" ")))
    if a.count("apple") > 1:
        print(a.index("apple", a.index("apple") + 1))
    else:
        print("Вхождений Меньше)")
def z3():
    a = list(map(int, input().split(" ")))
    if 0 in a:
        a.pop(0)
        print(a)
    else:
        print("Нолика нет")
def z4():
    a = list(map(str, input().split()))
    counta = 0
    countan = 0
    coubtthe = 0
    if "a" in a:
        counta = a.count("a")
    if "an" in a:
        countan = 0
    if "the" in a:
        coubtthe = 0
    print(f"a: {counta}, an: {countan}, the: {coubtthe}")
def z5():
    a = list(map(int, input().split(" ")))
    b = []

    for i in range(0, len(a)):
        try:
            x = a.index(0, i)
            b.append(x)
        except ValueError:
            b.remove(len(b)-1)
    print(b)
def z6():
    a = list(map(int, input().split(" ")))
    a.sort()
    b = int(input())
    a.append(b)
    a.sort()
    print(a)
def z7():
    n = int(input())
    a = list(map(str, input().split()))

    for i in a:
        if a.count(i) > n:
            print(i)
def z8():
    a = input()
    b = list(a)
    b.reverse()
    b = "".join(b)
    if a == b:
        print("YES")
    else:
        print("NO")
def z9():
    a = input()
    s = input()
    b = a.replace(s, "")
    print(b)
z9()