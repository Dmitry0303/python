num = int(input('Введите число '))
sum = num % 10
mul = num % 10
num //= 10
sum += num % 10
mul *= num % 10
num //= 10
sum += num
mul *= num
print(f"Сумма цифр: {sum}, произведение цифр: {mul}")
