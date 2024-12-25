a, b = int(input()), int(input())
def evklidnod(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def nok(a, b):
    return (a * b) // evklidnod(a, b)

if evklidnod(a, b) == 1:
    print("YES")
    print(nok(a, b))
else:
    print("NO")
    print(nok(a, b))jkj