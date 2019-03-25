max_num = 0
max_sum = 0


def get_sum(num: int):
    sum = 0
    while num != 0:
        sum += num % 10
        num //= 10
    return sum


while True:
    try:
        num = int(input("Введите натуральные числа через Enter, для выхода введите букву \n"))
        if num <= 0:
            raise ValueError
        else:
            if get_sum(num) > max_sum:
                max_num = num
                max_sum = get_sum(num)
            continue
    except ValueError:
        break


print(f"Число с наибольшей суммой цифр: {max_num}, его сумма цифр: {max_sum}")
