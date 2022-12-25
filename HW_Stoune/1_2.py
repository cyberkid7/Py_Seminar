# 1. Напишите программу для проверки ложности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (not (x or y or z) == (not x and not y and not z)):
                print(x, y, z)
