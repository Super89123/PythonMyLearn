def z1():
    a = int(input())
    print(list(range(1, a+1)))
def z2():
    a = [23, 43, 424 ,341, 232, 42123, 34234, 343234, 24343, 123432]
    print(a[0:7])
def z3():

    a = [23, 43, 424 ,341, 232, 42123, 34234, 343234, 24343, 123432]
    print(a[1:7])
def z4():

    a = [23, 43, 424 ,341, 232, 42123, 34234, 343234, 24343, 123432]
    print(max(a) + min(a))
def z5():

    a = [23, 43, 424 ,341, 232, 42123, 34234, 343234, 24343, 123432]
    print(sum(a) / len(a))
def z6():
    rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
    rainbow[0:7:2] = ["Красный","Желтый", "Синий" ,"Фиолетовый"]
    print(rainbow)
def z7():
    a = [1,2,3]
    a *= 2
    a += [6] * 9
    a += list(range(7, 14))
    print(a)
def z8():
    a = list(range(4, 14))
    if 5 in a and 17 in a:
        print("YES")
    else:
        print(sum(a[0:5]), sum((a[5:10])))


z7()