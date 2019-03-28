import random
N = 10
array = []
for i in range(N):
    array.append(random.randint(-10, 10))
min_i, minmin_i = 0, 0
min, minmin = array[min_i], array[minmin_i]
for i, num in enumerate(array):
    if num < minmin:
        minmin = num
        minmin_i = i

for i, num in enumerate(array):
    if num < min and i != minmin_i:
        min = num
        min_i = i

print(array)
print(f"Наименьшие элементы массива: {minmin}, {min}")
print(f"Индексы наименьших элементов: {minmin_i} {min_i}")
