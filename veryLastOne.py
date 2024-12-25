a = int(input())
a2 = 0
a3 = 0
a4 = 0
x1 = []
while a != 0:
    d = a % 10
    x1.append(d**2)
    a //= 10
a1 = sum(x1)
x1.clear()
while a1 != 0:
    d = a1 % 10
    x1.append(d**2)
    a1 //= 10
a2 = sum(x1)
x1.clear()
while a2 != 0:
    d = a2 % 10
    x1.append(d**2)
    a2 //= 10
a3 = sum(x1)
x1.clear()
while a3 != 0:
    d = a3 % 10
    x1.append(d**2)
    a3 //= 10
a4 = sum(x1)
x1.clear()
if a4 == 1:
    print("Число счастливое")
else:
    print("Чичло не  счастливое")