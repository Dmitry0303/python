import math

list1 = [-5, 25, 6, -9, -1, 2, 0]
list2 = []
for i in list1:
    if i < 0 or math.sqrt(i) % 1 != 0:
        continue
    else:
        list2.append(math.sqrt(i))
print(list2)
