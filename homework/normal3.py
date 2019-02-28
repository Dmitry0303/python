import random

n = int(input("Введите количетсво случайных чисел "))
numbers = []
for i in range(n):
    numbers.append(random.randint(-100, 100))
print(numbers)
