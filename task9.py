a = float(input("Введите первое число "))
b = float(input("Введите первое число "))
c = float(input("Введите первое число "))

if a < b < c or c < b < a:
    print(f"Среднее b = {b}")
elif b < a < c or c < a < b:
    print(f"Среднее a = {a}")
elif b < c < a or a < c < b:
    print(f"Среднее c = {c}")
else:
    print("Нет среднего")
