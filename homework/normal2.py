number1 = int(input("Введите 1-е число "))
number2 = int(input("Введите 2-е число "))
tmp = number2
cnt = 1
while tmp // 10 != 0:
    cnt = cnt + 1
    tmp = tmp // 10
number1 *= 10**cnt
number1 += number2
number2 = number1
number1 = number2 % 10**cnt
number2 = number2 // 10**cnt
print(number1)
print(number2)
