# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.

from random import sample

def words_list(num, word='abc'):
    w_list = []
    for i in range(num):
        m = sample(word, k=3)
        w_list.append("".join(m))
    return w_list

n = int(input('Введите число: '))

u = words_list(n)
print(u)
