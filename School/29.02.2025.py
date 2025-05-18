def z1():
    matrix = [[12312,342312,23121,423231],
              [34231,423122,24312,231234],
              [42312,34214,54342344,42321]]
    sum1 = 0
    for i in range(3):
        sum1 += sum(matrix[i])
    print(sum1)
def z2():
    matrix = [[12312, 342312, 23121, 423231],
              [34231, 423122, 24312, 231234],
              [42312, 34214, 54342344, 42321]]
    lastmax = 0
    for i in range(3):
        if max(matrix[i]) > lastmax:
            lastmax = max(matrix[i])
    print(lastmax)
def z3():
    matrix = [[12312, 342312, 23121, 423231],
              [34231, 423122, 24312, 231234],
              [42312, 34214, 54342344, 42321]]

    for j in range(3):
        for i in range(4-1):
            print(matrix[i][j], end = " ")
        print()




z3()