# Задача A
# Задана натуральная степень k. Сформировать случайным образом список \
#     коэффициентов (значения от 0 до 100) многочлена и записать в файл \
#         многочлен степени k.
# Пример:
#     k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0.

from random import randint

def write_file(st_r):
    with open('task4.txt', 'w', encoding='utf-8') as data:
        data.write(st_r)

def find_str(k):
    lst = []
    for i in range(k + 1):
        lst.append(randint(0, 101))
    return lst

def create_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst) - i - 1}'
                if lst[i + 1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i + 1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

k = int(input('Введите степень k = '))
koef = find_str(k)
write_file(create_str(koef))
