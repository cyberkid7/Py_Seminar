# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.56 -> 11


number = float(input('Введите вещественное число: '))
num = len(str(number))
number = number * 10 ** (num - 4)
sum_num = 0
for i in str(number):
    if i != ".":
        sum_num += int(i)

print(number, ' -> ', sum_num)
