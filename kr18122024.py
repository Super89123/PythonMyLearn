def z1():
    spisok = []
    for i in range(1, 16):
        if i % 2 != 0:
            spisok.append(0)
        else:
            spisok.append(i)
    print(spisok)
def z2():
    a = list(map(str, input().split(" ")))
    mina = ""
    spisokchet = []
    for i in a:
        chet = 0
        for j in a:
            if i == j:
                chet+=1
        spisokchet.append(chet)

    for i in range(len(spisokchet)):
        if spisokchet[i] == min(spisokchet):
            mina = a[i]
            break
    chet2 = 0
    for i in a:
        if i == mina:
            chet2+=1
    print(f"{mina}, Кол-во вхождений: {chet2}")
    print(spisokchet)
def z3():
    a = list(map(str, input().split(" ")))
    n = int(input())
    spisokchet = []
    for words in a:
        chet = 0
        for j in a:
            if j == words:
                chet+=1
        spisokchet.append(chet)
    for i in range(len(spisokchet)):
        if spisokchet[i] > n:
            a[i] = 0

    print(a)
def z4():
    a = list(map(str, input().split()))
    itog = []
    for word in a:
        word = word.upper()
        sorted_word = ''.join(sorted(word, reverse=True))

        itog.append(sorted_word)
    print(itog)
def z5():
    a = [i for i in range(10, 70)]
    print(a)
z5()