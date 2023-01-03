# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

number = int(input('Введите число: '))

def fib(n):
    find_list = []
    fib1 = 0
    fib2 = 1
    for i in range(number):
        fib1, fib2 = fib2, fib1 + fib2
        find_list.append(fib1)
    return find_list


print(fib(number))