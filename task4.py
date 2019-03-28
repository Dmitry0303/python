import random
max_cnt, num, cnt = 0, 0, 0
maxs = {}
N = 10
array = []

for i in range(N):
    array.append(random.randint(-10, 10))

for i in range(len(array)):
    if array[i] in maxs.keys():
        continue
    for j in range(len(array)):
        if array[i] == array[j]:
            cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
        maxs.clear()
        maxs[array[i]] = cnt
    elif cnt == max_cnt:
        maxs[array[i]] = cnt
    cnt = 0

print(array)
print("Число\t\t\tКоличество")
for i, j in maxs.items():
    print(f"{i:3}\t\t\t{j:10}")
