number = int(input("Введите номер числа Фибоначчи "))
num1 = 0
num2 = 1
if number <= 0:
    print("Ошибка")
elif number == 1:
    print("0")
elif number == 2:
    print("1")
else:
    for i in range(number - 2):
        result = num1 + num2
        num1 = num2
        num2 = result
    print(result)
