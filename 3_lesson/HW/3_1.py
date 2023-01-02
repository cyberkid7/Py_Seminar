# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
from random import randint

def find_sum(num):
    spisok = []
    for i in range(0, num):
        spisok.append(randint(1, 100))

    sum_num = 0
    for i in spisok:
        if spisok.index(i) % 2 == 0:
            sum_num = sum_num + i
    print(spisok, '\n', sum_num)

find_sum((int(input('Введите целое число: '))))
