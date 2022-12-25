#  Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
#  (или на какой оси она находится).

print("Enter the X coordinate with the exception of 0: ")
x = int(input())
print("Enter the Y coordinate with the exception of 0: ")
y = int(input())

if x == 0 or y == 0:
    print("Re-enter a coordinate greater than 0.")

if x > 0 and y > 0:
    print("x =", x, "y =", y, "-> 1")
elif x < 0 and y > 0:
    print("x =", x, "y =", y, "-> 2")
elif x < 0 and y < 0:
    print("x =", x, "y =", y, "-> 3")
elif x > 0 and y < 0:
    print("x =", x, "y =", y, "-> 4")