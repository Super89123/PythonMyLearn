def evklidnod(a,b):
    while b != 0:  # пока есть на что делить
        a, b = b, a % b
    return a
def evklidnok(a,b):
    return (a * b) // evklidnod(a, b)
a = int(input())
b = int(input())
print(evklidnod(a,b))
print(evklidnok(a,b))