#Сортировка методом слияния

import random
N = 1000
array = [random.random()*50 for _ in range(N)]


def merge_sort(array):
    if len(array) == 1 or len(array) == 0:
        return array
    else:
        array1 = merge_sort(array[:len(array) // 2])
        array2 = merge_sort(array[len(array) // 2:])
        array3 = []
        i, j = 0, 0
        for k in range(len(array1) + len(array2)):
            if i > len(array1) - 1:
                array3.append(array2[j])
                j += 1
            elif j > len(array2) - 1:
                array3.append(array1[i])
                i += 1
            elif array1[i] > array2[j]:
                array3.append(array2[j])
                j += 1
            elif array1[i] <= array2[j]:
                array3.append(array1[i])
                i += 1
        return array3


print(f"Исходный массив: {array}")
print(f"Отсортированный массив: {merge_sort(array)}")
