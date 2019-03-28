import random
N = 10
array1 = []
array2 = []
for i in range(N):
    array1.append(random.randint(-10, 10))

for i in range(len(array1)):
    if array1[i] % 2 == 0:
        array2.append(i)
print(f"Исходный массив: {array1}")
print(f"Индексы четных элементов: {array2}")
