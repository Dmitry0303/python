number = int(input("Введите число "))
while number // 10 != 0:
    tmp = number % 10
    number = number // 10
    print(tmp)
print(number)
