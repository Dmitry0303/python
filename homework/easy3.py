list1 = [1, 5, 3, 8, 0, 4, 3, 2]
list2 = []
for i in list1:
    if(i % 2 == 0):
        list2.append(i / 4)
    else:
        list2.append(i*2)
print(list2)
