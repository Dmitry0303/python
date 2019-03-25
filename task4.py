while True:
    try:
        n = int(input("Введите количество элементов ряда: "))
        if n <= 0:
            raise ValueError("Количество должео быть целым положительным числом")
        else:
            break
    except ValueError as e:
        print(e)
        continue

num = 1.0
sum = 1.0
for i in range(n - 1):
    num = -num/2
    sum = sum + num
print(f"Сумма элементов ряда: {sum}")
