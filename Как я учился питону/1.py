import random

b = random.uniform(0,99999999)
c = round(b)

k = input('Сколько раз вы хотите воспользоваться программой? ')
for i in range(99999999):
    b = random.uniform(0,99999999)
    c = round(b)
    a = input('Введите текст: ')
    print(f"print(f'{a} ')")
    print(f"input(f'{a} ')")
    print(f"{c} = print(f'{a} ')")
    print(f"{c} = input(f'{a} ')")
    
