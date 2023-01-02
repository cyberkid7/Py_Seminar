# 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.

from random import randint

def find_sum(num):
    spisok = []
    for i in range(0, num):
        spisok.append(randint(1, 100))

    sum_num = 0
    # for i in spisok(0, num, 2):
    #     sum_num = sum_num + i
    # print(spisok, '\n', sum_num)
    for i in spisok:
        if spisok.index(i) % 2 != 0:
            sum_num = sum_num + i
    print(spisok, '\n', sum_num)

find_sum((int(input('Введите целое число: '))))