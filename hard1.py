number = int(input("Введите число "))
left = 2
right = number // 2
for i in range(2, right + 1):
    if number % i == 0:
        print("Число непростое")
        break
    elif i == right:
        print("Число простое")
