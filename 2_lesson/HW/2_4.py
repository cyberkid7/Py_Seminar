# 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

n = int(input('Enter the value of N: '))
num_list = list(range(-n, n + 1))

print(num_list)

int_first = int(input('Enter position one: '))
int_second = int(input('Enter position two: '))

len_list = len(num_list)

if len_list >= int_first > 0 and len_list >= int_second > 0:
    print(num_list[int_first - 1] * num_list[int_second - 1])
else:
    print('There are not values for these indexes!')


# for i in range(-n, n + 1):


