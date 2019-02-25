import math
a = int(input("Введите a "))
b = int(input("Введите b "))
c = int(input("Введите b "))
d = b*b - 4*a*c
if d < 0:
    print("Вещественных корней нет")
else:
    x1 = (-b - math.sqrt(d)) / 2 * a
    x2 = (-b + math.sqrt(d)) / 2 * a
    print("Корни уравнения: ", x1, x2)

