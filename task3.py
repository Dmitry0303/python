'''Приведены пять методов сортировок и проведены исследования их скорости и сложности
Размер массива N        Пузырьковый, сек    Выбором, сек    Вставкой, сек   Быстрая, сек    Слиянием, сек
100                     0,00312             0,0015          0,0014          0,000723        0,00125
1000                    0.247               0.099           0.0931          0.00581         0.00913
10000                   17.17               9.0             7.857           0.0951          0.1171
Сложность               n^2                 n^2             n^2             nlogn           nlogn
'''

import random
import timeit
import sys
sys.setrecursionlimit(1500)
N = 10000
array_ = [random.randint(-100, 99) for _ in range(N)]


#Сортировка пузырьковым методом
def bubble_sort(array):
    for i in range(1, len(array)):
        flag = False
        for j in range(len(array) - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        if not flag:
            break


#Сортировка выбором
def select_sort(array):
    for i in range(len(array)):
        ind_min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[ind_min]:
                ind_min = j
        array[i], array[ind_min] = array[ind_min], array[i]


#Сортировка вставками
def insert_sort(array):
    for i in range(1, len(array)):
        tmp = array[i]
        j = i - 1
        while tmp < array[j] and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = tmp


#Быстрая сортировка
def quick_sort(array):
    if len(array) == 1 or len(array) == 0:
        return array
    else:
        pivot = array[0]
        i = 0
        for j in range(len(array) - 1):
            if array[j + 1] < pivot:
                array[j + 1], array[i + 1] = array[i + 1], array[j + 1]
                i += 1
        array[0], array[i] = array[i], array[0]
        first_part = quick_sort(array[:i])
        second_part = quick_sort(array[i + 1:])
        first_part.append(array[i])
        return first_part + second_part


#Сортировка слиянием
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


array = array_[:]
bubble = timeit.timeit("bubble_sort(array)", setup="from __main__ import bubble_sort, array", number=1)
array = array_[:]
select = timeit.timeit("select_sort(array)", setup="from __main__ import select_sort, array", number=1)
array = array_[:]
insert = timeit.timeit("insert_sort(array)", setup="from __main__ import insert_sort, array", number=1)
array = array_[:]
quick = timeit.timeit("quick_sort(array)", setup="from __main__ import quick_sort, array", number=1)
array = array_[:]
merge = timeit.timeit("merge_sort(array)", setup="from __main__ import merge_sort, array", number=1)

print(f"Пузырьковым методом сортировка выполнена за {bubble}")
print(f"Методом выборки сортировка выполнена за {select}")
print(f"Методом вставки сортировка выполнена за {insert}")
print(f"Быстрой сортировкой сортировка выполнена за {quick}")
print(f"Сортировкой слиянием сортировка выполнена за {merge}")

