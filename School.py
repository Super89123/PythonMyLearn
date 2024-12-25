

def nok(a,b):
    if a > b:
        greater = a
    else:
        greater = b
    while True:
        if (greater % a == 0) and (greater % b == 0):
            nokd = greater

            break
        greater += 1
    return nokd

print(nok(int(input()), int(input())))