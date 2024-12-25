def nod(a, b):
    lesser = min(a,b)
    for i in range(1, lesser + 1):
        if ((a % i == 0) and (b % i == 0)):
            nod1 = i
    return nod1
print(nod(int(input()), int(input())))