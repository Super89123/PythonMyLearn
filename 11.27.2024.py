def z1():
    a = list(map(str, input().split()))
    for elem in a:
        print(elem)
def z2():
    a = input().split()

    itog = []
    for elem in a:
        itog.append(elem[0])
    print('.'.join(itog) + ".")
def z3():
    a = input().split('\\')
    for elem in a:
        print(elem)

def z4():
    a = list(map(int, input().split()))
    for elem in a:
        print("+"*elem)

def z5():
    a = list(map(int, input().split(".")))
    sum = 0
    for elem in a:
        if 0 <= elem <= 255:
            sum+=1
    if sum == 4:
        print("YES")
    else:
        print("NO")
def z6():
    a = input().split()
    b = input()
    print(b.join(a))

def z7():
    a = int(input())
    b = []
    for i in range(a):
       x = input().split()
       b.append(x)

    poisk = input().split()
    for elem in b:
        if poisk in elem:
            print(elem)
    print(b)

z7()