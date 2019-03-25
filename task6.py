import random
steps = 10
min = 0
max = 100
x = random.randint(min, max)
print(f"Было загадано число от {min} до {max}. Попробуй отгадать его за {steps} шагов")
for i in range(steps):
    print(f"У тебя осталось {steps - i} шагов")
    while True:
        try:
            num = int(input(f"Введи целое число от {min} до {max} "))
            if num < min or num > max:
                raise ValueError
            else:
                break
        except ValueError:
            continue

    if num != x and i == steps - 1:
        print(f"Ты проиграл. Шаги закончились. Было загадоно число: {x}")
        break
    if num > x:
        print("Загаданное число меньше введенного")
        continue
    elif num < x:
        print("Загаданное число больше введенного")
        continue
    else:
        print(f"Ты выиграл! Загаданное число: {x}")
        break
