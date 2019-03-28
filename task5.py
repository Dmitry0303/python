import random
N = 10
array = []
for i in range(N):
    array.append(random.randint(-10, 10))
max_i = 0
max = array[max_i]

for i in range(1, len(array)):
    if max < array[i] < 0:
        max = array[i]
        max_i = i

print(array)
print(f"Наибольший отрицательный элемент массива: {max}, его индекс: {max_i}")
