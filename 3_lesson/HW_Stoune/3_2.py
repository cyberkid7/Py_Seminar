# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint

# number = int(input('Введите целое число: '))

def find_list(number):
    list_num = []
    for i in range(0, number):
        list_num.append(randint(1, 10))
    print(list_num)
    return list_num


def twin_multi(spisok):
    kol = len(spisok)
    for i in range(0, int(kol/2)):
        print(spisok[i], ',', spisok[kol-i-1], '=>', spisok[i] * spisok[kol-i-1])
    if kol % 2 == 1:
        print(spisok[(kol // 2)])


number = int(input('Введите целое число: '))
spisok = find_list(number)

twin_multi(spisok)
