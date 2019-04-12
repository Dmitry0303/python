#Сортировка пузырьковым методом

import random
N = 1000
array = [random.randint(-100, 99) for _ in range(N)]


def bubble_sort(array):
    for i in range(1, len(array)):
        flag = False
        for j in range(len(array) - i):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        if not flag:
            break


print(f"Исходный массив: {array}")
bubble_sort(array)
print(f"Отсортированный массив: {array}")

