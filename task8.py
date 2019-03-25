str1 = ''
cnt = 0
while True:
    try:
        n = int(input("Введите количество чисел "))
        if n <= 0:
            raise ValueError
        else:
            break
    except ValueError:
        continue

while True:
    try:
        x = int(input("Введите искомую цифру "))
        if x < 0:
            raise ValueError
        else:
            x = str(x)
            break
    except ValueError:
        continue

print(f"Введите {n} целых чисел через Enter ")
while True:
    try:
        str1 += str(int(input())) + ' '
        n -= 1
        if n == 0:
            break
        else:
            print(f"Введите {n} целых чисел через Enter ")
    except ValueError:
        print(f"Введите {n} целых чисел через Enter ")
        continue

for i in str1:
    if i == x:
        cnt += 1

print(f"В числах {str1} цифра {x} встречается {cnt} раз")
