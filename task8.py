year = int(input("Введите год: "))
if year % 400 == 0:
    print("Високосный год")
elif year % 100 == 0:
    print("Невисокосный год")
elif year % 4 == 0:
    print("Високосный год")
else:
    print("Невисокосный год")
