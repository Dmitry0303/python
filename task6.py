import random
N = 10
array = []
for i in range(N):
    array.append(random.randint(-10, 10))
max_i, min_i, sum = 0, 0, 0
min, max = array[min_i], array[max_i]
for i in range(1, len(array)):
    if array[i] < min:
        min = array[i]
        min_i = i
    if array[i] > max:
        max = array[i]
        max_i = i

for i in range(len(array)):
    if min_i > i > max_i or min_i < i < max_i:
        sum += array[i]

print(array)
print(f"Максимальный элемент: {max}, минимальный элемент: {min}")
print(f"Индекс максимального элемента: {max_i}, индекс минимального элемента: {min_i}")
print(f"Сумма элементов, находящихся между максимальным и минимальным элементами: {sum}")