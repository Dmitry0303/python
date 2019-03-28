import random
I, J = 5, 5
matr = []
min = []
for i in range(I):
    row = []
    for j in range(J):
        num = random.randint(-10, 10)
        row.append(num)
        if i == 0:
            min.append(num)
        elif num < min[j]:
            min[j] = num
    matr.append(row)

for row in matr:
    for num in row:
        print(f"{num:5}", end='')
    print('\n')
print('-'*27)

max = min[0]

for num in min:
    print(f"{num:5}", end='')
    if num > max:
        max = num

print("\n")
print(f"Максимальный элемент среди минимальных элементов столбцов матрицы: {max}")
