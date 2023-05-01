import random

b = random.uniform(0,99999999)
c = round(b)

k = int(input('Сколько раз вы хотите воспользоваться программой? '))
for i in range(k):
    b = random.uniform(0,k)
    c = round(b)
    a = input('Введите текст: ')
    print(f"print(f'{a} ')")
    print(f"input(f'{a} ')")
    print(f"{c} = print(f'{a} ')")
    print(f"{c} = input(f'{a} ')")
    
