number = int(input("Введите число "))
if number // 10 == 0:
    print("Наибольшая цифра в числе ", number)
else:
    tmp = number % 10
    while True:
        max =  number % 10

        if tmp > max:
            max = tmp
        if number // 10 == 0:
            break
        number = number // 10
print(max)
