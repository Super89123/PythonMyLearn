from itertools import count


def draw_box():
    print("*" * 10)
    for i in range(12):
        print("*        *")
    print("*" * 10)
#draw_box()
def draw_triangle():
    for i in range(11):
        print("*"*i)
#draw_triangle()
def generate_squares():
    a = []
    for i in range(1, 11):
        a.append(i**2)
    print(a)
#generate_squares()
def filter_even_numbers():
    a = []
    itog = []
    for i in range(1, 133):
        a.append(i)
    for elem in a:
        if elem % 2 == 0:
            itog.append(elem)
    print(itog)
#filter_even_numbers()
def count_vowels():
    a = "Всем привет ребята!"
    glas = "ёуеаоэяи"
    counter = 0
    for elem in a:
        if elem in glas:
            counter+=1
    print(counter)
#count_vowels()
def multiplication_table():
    for i in range(1, 6):
        for j in range(1, 6):
            print(f"{i} * {j} = " + str(i*j), end=" ")
        print()

#multiplication_table()
def longest_word():
    a = ["Хихихихих", "Вова", "Устал"]
    longs = ""
    for elem in a:
        if len(elem) > len(longs):
            longs = elem
    print(longs)
longest_word()