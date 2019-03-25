step = 0
sum = 0
while True:
    try:
        num = int(input(f"Введи целое число больше 0 "))
        if num <= 0:
            raise ValueError
        else:
            break
    except ValueError:
        continue

for i in range(num):
    step += 1
    sum += step

print(f"1 + 2 + .. + n = {float(sum)}")
print(f"n*(n+1)/2 = {num * (num + 1)/2}")
