def factors(num):
    a = []
    for i in range(1, num+1):
        if num % i == 0:
            a.append(i)
    return a
print(factors(10))
def find_all(target, symbol):
    b = []
    for i in range(len(target)):
        if symbol == target[i]:
            b.append(i)
    return b
def merge(list1, list2):
    itog = list1+list2
    itog.sort()
    return itog
def sum_matrixes(a, b):
    s = 0
    if len(a) == len(b):
        if len(a[0]) == len(b[0]):
            for i in range(len(a)):
                for j in range(len(b)):
                    s += a[i][j]
                    s += b[i][j]
        else:
            return  None
    else:
        return None
    return s

print(sum_matrixes([
    [1,2,3],
    [4,5,6],
    [7,8,9]
], [
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
]))
def rotate_matrix_90(matrix):
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[j][n - 1 - i] = matrix[i][j]
    return rotated
def list_difference(list1, list2):
    itog = []
    for elem in list1:
        if elem not in list2:
            itog.append(elem)

    return itog
def filter_by_length(lists, min_length):
    itog = []
    for lit in lists:
        if len(lit ) >= min_length:
            itog.append(lit)
    return itog

print(list_difference([1,2,3], [2,3,4,5,6]))

print(merge([1,2,3], [2,3,4]))