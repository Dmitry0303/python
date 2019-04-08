'''Первый вариант программы поиска максимального и минимального
элементов массива. Используется кортеж, а также есть
промежуточные переменные min и max. Версия Python - 3.7. Разрядность системы - 64'''

from pympler import asizeof

array = [4, 8, 0, 2, -3, 2, -5, -9, 6, -1]
min_ind, max_ind = 0, 0
min, max = array[0], array[0]

for i in range(1, 10):
    if array[i] > max:
        max = array[i]
        max_ind = i
    if array[i] < min:
        min = array[i]
        min_ind = i

print(array)
print(f"Минимальный элемент массива: {min} находится на {min_ind} позиции")
print(f"Максимальный элемент массива: {max} находится на {max_ind} позиции")
print(f"array занимает: {asizeof.asizeof(array)} байт")
print(f"min_ind занимает: {asizeof.asizeof(min_ind)} байт")
print(f"max_ind занимает: {asizeof.asizeof(max_ind)} байт")
print(f"min занимает: {asizeof.asizeof(min)} байт")
print(f"max занимает: {asizeof.asizeof(max)} байт")
print(f"Общий размер памяти: {asizeof.asizeof(max_ind) + asizeof.asizeof(min_ind) + asizeof.asizeof(array) + asizeof.asizeof(min) + asizeof.asizeof(max)} байт")
