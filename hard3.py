n = int(input("Введите n "))
m = int(input("Введите m "))
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            print('AAA', end='')
            print('BBB', end='')
        print('\n')
    else:
        for j in range(m):
            print('BBB', end = '')
            print('AAA', end = '')
        print('\n')