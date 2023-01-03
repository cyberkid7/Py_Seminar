# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов, отличной от 0.

import random
from math import modf


def find_list(number):
    list_num = []
    for i in range(number):
        list_num.append(round(random.uniform(1, 10), 2))
    print(list_num)
    return list_num


def find_difference(name):
    new_list = []
    for i in name:
         new_list.append(round(modf(i)[0], 2))
    # print(new_list)
    new_list.sort()
    # print(new_list)
    res = round(new_list[-1] - new_list[0], 2)
    return res


number = int(input('Введите целое число: '))
spisok = find_list(number)


print(find_difference(spisok))

