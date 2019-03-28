cnt = 0
for i in range(2, 99):
    for j in range(2, 9):
        if i % j == 0:
            cnt += 1

print(f"Количество кратных чисел: {cnt}")
