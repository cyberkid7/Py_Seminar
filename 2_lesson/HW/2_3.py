# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in # 6
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

num = int(input('Введите целое число: '))
number_list = []
sum_numbers = 0
for i in range(1, num + 1):
    res = round((1 + 1 / i)** i, 2)
    number_list.append(res)
    sum_numbers += res

print(number_list)
print(sum_numbers)