a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
n = int(input())
sp = []
daysyear = 0
if c == f:
    for i in range(n):
        x = int(input())
        daysyear += x
        sp.append(x)
    daysSince = 0
    for i in range(1, b + 1):
        daysSince += sp[i]
    daysSince += a
    dayspast = 0
    for i in range(1, e+1):
        dayspast += sp[i]
    dayspast += d
    print(dayspast - daysSince)

else:
    for i in range(n):
        x = int(input())
        daysyear += x
        sp.append(x)
    daysSince = 0
    for i in range(1, b + 1):
        daysSince += sp[i]
    daysSince += a
    dayspast = 0
    for i in range(1, e+1):
        dayspast += sp[i]
    dayspast += d
    dayspast += (f-c) *daysyear
    print(dayspast - daysSince+1)