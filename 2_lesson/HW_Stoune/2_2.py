# 2. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in # 4
# out
# [2.0, 2.25, 2.37, 2.441]
# 9.06

num = int(input('Введите целое число: '))
number_list = []
sum_numbers = 0
for i in range(1, num + 1):
    res = round((1 + 1 / i)** i, 2)
    number_list.append(res)
    sum_numbers += res

print(number_list)
print(sum_numbers)