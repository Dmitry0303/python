num = input("Введите число: ")
even = 0
odd = 0
for i in num:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Количество четных цифр {even}")
print(f"Количество нечетных цифр {odd}")

