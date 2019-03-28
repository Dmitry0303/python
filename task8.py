I, J = 5, 4
sum = 0
matr = []
for i in range(I):
    row = []
    for j in range(J - 1):
        while True:
            try:
                num = int(input(f"Введите {j}-й элемент {i}-й строки "))
                break
            except ValueError:
                print("Введите целое число")
                continue
        row.append(num)
        sum += num
    row.append(sum)
    sum = 0
    matr.append(row)

for row in matr:
    for num in row:
        print(f"{num:5}", end=' ')
    print("\n")
