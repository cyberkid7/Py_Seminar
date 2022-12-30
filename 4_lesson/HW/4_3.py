# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.

from random import randint


number = int(input('Введите целое число: '))
spisok = []

for i in range(0, number):
    spisok.append(randint(1, 9))

newspisok = []
for a in (spisok):
    if spisok.count(a) == 1:
        newspisok.append(a)

print(spisok)
print(newspisok)