def z1():
    matrix = [[452, 42334, 24245],
              [3423224, 4314, 5143],
              [3423, 423452, 423212]]

    itog = []
    for i in range(3):
        for c in range(3):
            if i > c:
                itog.append(matrix[i][c])
    print(max(itog))
def z2():
    matrix = [[452, 42334, 24245, 52311],
              [3423224, 4314, 5143, 5413234],
              [3423, 423452, 423212, 542313423],
              [2413324,431234,42321,5431324]]

    itog = []
    for i in range(4):
        for c in range(4):
            if c < i < 4-c-1:
                itog.append(matrix[i][c])
            if c > i > 4-1-c:
                itog.append(matrix[i][c])
    print(max(itog))
def z3():
    matrix = [[452, 42334, 24245, 52311],
              [3423224, 4314, 5143, 5413234],
              [3423, 423452, 423212, 542313423],
              [2413324, 431234, 42321, 5431324]]

    itog = []
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    for i in range(4):
        for c in range(4):
            if c > i > 4 - c - 1:
                sum2+=matrix[i][c]
            if c > i > 4 - 1 - c:
                sum3 += matrix[i][c]
            if i < c and i < 4 - c - 1:
                sum1 += matrix[i][c]
            if c < i < 4 - c - 1:
                sum4 += matrix[i][c]
    print(f'Верх: {sum1}')
    print(f'Право: {sum2}')
    print(f'Низ: {sum3}')
    print(f'Лево: {sum4}')
def z4():
    n = int(input())
    matrix = [[0] * n for i in range(n)]
    for i in range(n):
       matrix[i][n-1-i] = 1
    for i in range(n):
        for c in range(n):
            if c > i > 4 - c - 1:
                matrix[i][c] = 2
            if c > i > 4 - 1 - c:
                matrix[i][c] = 2
            if i < c and i < 4 - c - 1:
               matrix[i][c] = 0
            if c < i < 4 - c - 1:
                matrix[i][c] = 0
    for i in range(n):
        for c in range(n):
            print(matrix[i][c], end= " ")
        print()



z4()