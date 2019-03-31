'''
Пример из второго пункта 3-го ДЗ
Время работы старой функции: 2,46 - размер списка: 1000
Время работы новой функции: 1,53  - размер списка: 1000
Время работы старой функции: 11,33 - размер списка: 5000
Время работы новой функции: 6,92  - размер списка: 5000
Время работы старой функции: 22,64 - размер списка: 10000
Время работы новой функции: 14,18  - размер списка: 10000
Сложность первого алгоритма - линейная O(0,0022n)
Сложность второго алгоритма - линейная O(0,0014n)
Скорость второго алгоритма выше, так как меньше обращений
к элементам списка.
'''


import random
import timeit
N = 5000
array1 = [random.randint(-10, 10) for _ in range(N)]


def old_func(a: list):
    b = []
    for i in range(len(a)):
        if a[i] % 2 == 0:
            b.append(a[i])
    return b


def new_func(a: list):
    b = []
    for i in a:
        if i % 2 == 0:
            b.append(i)
    return b


print(timeit.timeit("old_func(array1)", setup="from __main__ import old_func, array1", number=10000))
print(timeit.timeit("new_func(array1)", setup="from __main__ import new_func, array1", number=10000))
