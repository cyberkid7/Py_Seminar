# 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

from random import randrange

num = int(input('Введите целое число: '))
num_list = list(range(num))

print(num_list)

for i in range(num):
    n_1, n_2 = randrange(num), randrange(num)
    num_list[n_1], num_list[n_2] = num_list[n_2], num_list[n_1]

print(num_list)