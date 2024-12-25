from itertools import count


def z1():
    a = list(map(str, input().split(" ")))
    countChisl = 0
    countchar = 0
    for elem in a:
        for sostav in elem:
            if sostav.isdigit():
                countChisl+=1
            if sostav.isalpha():
                countchar+=1
    print(countChisl, countchar)
def z2():
    glasnie = "eyuioaEYUIOAуеёыаоэяиюЁУЕЫАОЭЯИЮ"
    soglasnie = "qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNMцкнгшщзхфвпрлдчсмтбйЙЦКНГШЩЗХФВПРЛДЖЧСМТБ"
    a = list(map(str, input().split(" ")))
    results = []
    for elem in a:
        chetG = 0
        chetS = 0
        for bykva in elem:
            if bykva in glasnie:
                chetG+=1
            if bykva in soglasnie:
                chetS+=1
        if chetG == chetS:
            results.append(elem)
            print(elem)
def z3():
    znaki = """
            (!?.,-;:'")
            """
    a = list(map(str, input().split(" ")))
    spisoknew = []
    count = 0
    for elem in a:
        stroka = elem


        for bykva in stroka:
            if bykva in znaki:
                stroka.replace(bykva, "")
        if stroka not in spisoknew:
            count+=1
            spisoknew.append(elem)
    print(spisoknew, count)

z3()