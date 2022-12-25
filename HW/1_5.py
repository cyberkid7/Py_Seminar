# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

print("Введите координаты точки А:")
xA = int(input())
yA = int(input())

print("Введите координаты точки B:")
xB = int(input())
yB = int(input())

distance = sqrt((xB - xA)**2 + (yB - yA)**2)
print(distance)
