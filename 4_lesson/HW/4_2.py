# 2. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

def issimple(q):
    # проверка числа q на простоту
    for i in range(2, q):
        if q % i == 0:
            return False  # составное
    return True  # простое


def isimple(i):
    # возвращаем i-ое простое число:
    a = 2  # числа которые будут увеличиватья и проверяться на простоту
    n = 1  # счетчик простых чисел
    u = True
    while u:
        if issimple(a):
            if n == i:
                # print(f'{a} - простое №{n}')
                return a
                break
            n += 1
        a += 1


def simplemultiply(q):
    spisok = []
    n = 1
    while q > 1:
        if q%(isimple(n)) == 0:
            # print(f'{q} нацело делится на {isimple(n)}')
            spisok.append(isimple(n))
            q = q / isimple(n)
        else:
            n += 1
    return spisok

number = int(input('Введите число: '))
print(simplemultiply(number))