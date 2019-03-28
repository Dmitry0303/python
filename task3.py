import random
array = []
array.append(random.randint(-10, 10))
min_ind, max_ind = 0, 0
min, max = array[0], array[0]

for i in range(1, 10):
    array.append(random.randint(-10, 10))
    if array[i] > max:
        max = array[i]
        max_ind = i
    if array[i] < min:
        min = array[i]
        min_ind = i

print(f"Исходный массив: {array}")
print(f"Индекс наибольшего элемента: {max_ind}")
print(f"Индекс наименьшего элемента: {min_ind}")
array[max_ind], array[min_ind] = array[min_ind], array[max_ind]
print(f"Массив после смены мест максимального и минимального элементов: {array}")
