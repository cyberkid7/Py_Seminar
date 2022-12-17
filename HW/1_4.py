# Задача 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

print("Enter the quarter number from 1 to 4: ")
quarter = int(input())

if quarter > 4:
    print("There is no such quarter!")
elif quarter == 1:
    print("1 - x > 0, y > 0")
elif quarter == 2:
    print("2 - x < , y > 0")
elif quarter == 3:
    print("3 - x < 0, y < 0")
elif quarter == 4:
    print("1 - x > 0, y < 0")
