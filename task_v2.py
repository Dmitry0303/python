'''Второй вариант программы поиска максимального и минимального
элементов массива. Вместо списка используется кортеж, а также нет
промежуточных переменных min и max. На этом экономится 40 байт для
данного набора данных. Версия Python - 3.7. Разрядность системы - 64'''

from pympler import asizeof

array = (4, 8, 0, 2, -3, 2, -5, -9, 6, -1)
min_ind, max_ind = 0, 0

for i in range(1, 10):
    if array[i] > array[max_ind]:
        max_ind = i
    if array[i] < array[min_ind]:
        min_ind = i

print(array)
print(f"Минимальный элемент массива: {array[min_ind]} находится на {min_ind} позиции")
print(f"Максимальный элемент массива: {array[max_ind]} находится на {max_ind} позиции")
print(f"array занимает: {asizeof.asizeof(array)} байт")
print(f"min_ind занимает: {asizeof.asizeof(min_ind)} байт")
print(f"max_ind занимает: {asizeof.asizeof(max_ind)} байт")
print(f"Общий размер памяти: {asizeof.asizeof(max_ind) + asizeof.asizeof(min_ind) + asizeof.asizeof(array)} байт")




