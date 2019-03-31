'''
Пример из третьего пункта 3-го ДЗ
Время работы старой функции: 1,77 - размер списка: 1000
Время работы новой функции: 2,83  - размер списка: 1000
Время работы старой функции: 8,86 - размер списка: 5000
Время работы новой функции: 14,00  - размер списка: 5000
Время работы старой функции: 17,63 - размер списка: 10000
Время работы новой функции: 28,08  - размер списка: 10000
Сложность первого алгоритма - линейная O(0,0018n)
Сложность второго алгоритма - линейная O(0,0028n)
Скорость работы второго алгоритма ниже, так как больше
обращений к элементам списка. Зато меньше промежуточных переменных.
'''



import random
import timeit
N = 5000
array1 = [random.randint(-10, 10) for _ in range(N)]


def old_func(array: list):
    min_ind, max_ind = 0, 0
    min, max = array[0], array[0]
    for i in range(1, len(array)):
        if array[i] > max:
            max = array[i]
            max_ind = i
        if array[i] < min:
            min = array[i]
            min_ind = i
    return min_ind, max_ind


def new_func(array: list):
    min_ind, max_ind = 0, 0
    for i in range(1, len(array)):
        if array[i] > array[max_ind]:
            max_ind = i
        if array[i] < array[min_ind]:
            min_ind = i
    return min_ind, max_ind


print(timeit.timeit("old_func(array1)", setup="from __main__ import old_func, array1", number=10000))
print(timeit.timeit("new_func(array1)", setup="from __main__ import new_func, array1", number=10000))
