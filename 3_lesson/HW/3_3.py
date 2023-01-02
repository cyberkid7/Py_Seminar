# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

number = int(input('Введите целое число: '))

def dectobin(a):
    spisok = []
    while a > 0:
        b = a % 2
        spisok.append(b)
        a = int(a/2)
    return list(reversed(spisok))


a = dectobin(number)
print(a)
