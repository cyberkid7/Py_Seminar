# 1. Вычислить число c заданной точностью d

from decimal import Decimal

a = float(input('Enter a real number: '))
b = input('Enter the required accuracy: ')

c = Decimal(str(a))
print(c.quantize(Decimal(b)))