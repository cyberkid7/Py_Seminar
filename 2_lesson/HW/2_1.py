# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

number = float(input('Введите вещественное число: '))
num = len(str(number))
number = number * 10 ** (num - 4)
sum = 0
for i in str(number):
    if i != ".":
        sum += int(i)

print(number)
print(sum)
