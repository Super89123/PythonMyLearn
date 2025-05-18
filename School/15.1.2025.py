def z1():
    a = [['Понедельник', ['русский язык', 'математика']], ['Суббота', ['русский язык', 'математика']], ['Воскресенье', ['русский язык', 'математика']], ['Вторник', ['русский язык', 'математика']], ['Среда', ['русский язык', 'математика', 'физ-ра']], ['Четверг', ['русский язык', 'математика']], ['Пятница', ['русский язык', 'математика']]]
    for elem in a:
        if elem[0] == "Среда":
            for lem in elem[1]:
                print(lem)
def z2():
    a = [[432132, 665347283, 42134541],[ 56324173891, 354324, 543232],[345432, 5234543234, 5789134553]]
    newsp = []
    for elem in a:
        for lem in elem:
            newsp.append(lem)
    print(max(newsp))
def z3():
    a = [[1, 2 ,3 ], [4, 5 ,6 ], [7 , 8 ,9]]
    itog = []
    for elem in a:
        sp = []
        for i in range(len(elem)-1, -1, -1):
            sp.append(elem[i])
        itog.append(sp)
    print(itog)
def z4():
    a = [[1, 2, 3], [4, 5 ,6 ], [7 , 8, 9]]
    itog = []
    for elem in a:
        s = 0
        for lm in elem:
            s += lm
        itog.append(s)
    print(itog)
def z5():
    a = [[1, 2, 3], [1, 2, 2], [1, 1, 4]]
    print(sorted(a))
def z6():
    grades = [
        ["Анна", [3, 4, 5, 4]],
        ["Игорь", [5, 5, 4, 3]],
        ["Ольга", [4, 3, 3, 5]]
    ]
    sp = []
    for elem in grades:
         s = 0

         for lm in elem[1]:
             s += lm
         s /= len(elem[1])

         sp.append(s)
    print(grades[sp.index(max(sp))][0])


z6()