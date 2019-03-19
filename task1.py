coins = 5
is_first = True

while True:
    print(f"Осталось монет: {coins}")
    try:
        if is_first:
            coins_num = int(input("Игрок 1, возьмите монеты (от 1 до 3-х): "))
        else:
            coins_num = int(input("Игрок 2, возьмите монеты (от 1 до 3-х): "))
    except ValueError:
        print("Введите целое число от 1 до 3")
        continue
    if coins_num <= 0 or coins_num > 3:
        print("Введите целое число от 1 до 3")
        continue
    if coins_num > coins:
        print("Вы не можете взять монет больше, чем осталось")
        continue
    else:
        coins -= coins_num
        is_first = not is_first
        if coins == 0:
            if is_first:
                print("Выиграл Игрок 1")
                exit()
            else:
                print("Выиграл Игрок 2 ")
                exit()
