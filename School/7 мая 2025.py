

def find_min(list, ignore_negatives=False):
    k = []
    if(ignore_negatives):
        for elem in list:
            if elem >= 0:
                k.append(elem)
        return min(k)
    else:
        return min(list)
def remove_value(list, value, count=1):
    for i in range(count):
        list.remove(value)
    return list
def print_table(matrix, sep= '  ', end = '\n'):
    for i in matrix:
        for k in i:
            print(k, end = sep)
        print(sep)
def rounded_sum(lst, round_to=2):
    return round(sum(lst), round_to)
def create_matrix(rows, cols, fill=0):
    matrix = []
    for i in range(rows):
        matrix.append([fill for i in range(cols)])

    return matrix
def insert_into(lst, index, value, safe=True):
    if safe :
        if index > len(lst)-1:
            lst.append(value)
        else:
            lst.insert(index, value)
    else:
        if index > len(lst)-1:
            print("Я вышел за границы!")
        else:
            lst.insert(index, value)
def count_chars(strings, ingore_spaces=True):
    count = 0
    if ingore_spaces:
        for elem in strings:
            for s in elem:
                if s != ' ':
                    count+=1
    else:
        for elem in strings:
            for s in elem:

                    count+=1




print(find_min([-1, 0, 2, 3], ignore_negatives=True))
print(remove_value([1,2,1], 1, count=2))
print_table([[1,2,3],
             [4,5,6],
             [6,7,8]])
print(rounded_sum([1.111111, 34.324]))
print(create_matrix(3, 3))