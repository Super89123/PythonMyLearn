def evklidnod(a,b,c):
    while b != 0:  # пока есть на что делить
        a, b = b, a % b
    while c != 0:
        a, c = c, a % c
    return a

def evklidnod2(a,b):
    while b != 0:  # пока есть на что делить
        a, b = b, a % b
    return a
def evklidnok2(a, b):
    return a * b // evklidnod2(a, b)

def evklidnok3(a, b, c):
    return evklidnok2(a, evklidnok2(b, c))

def evklidnok(a, b, c):
    nod_ab = evklidnod2(a, b)
    nod_abc = evklidnod2(nod_ab, c)
    return (a * b * c) // nod_abc


a = int(input())
b = int(input())
c = int(input())
print(evklidnok3(a,b,c))
print(evklidnod(a,b,c))