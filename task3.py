'''
№ прост. числа    Без решета    С решетом
       100            0.43          0.25
       200            1.07          0.65
       500            4.17          2.29
       1000           11.04         5.9
       2000           30.29         16.46
       4000           88.67         41.44
сложность алгоритмов нелинейная- O(nlogn)
'''

import timeit
N = 4000


def is_simple(n):
    tmp = 3
    try:
        if int(n) <= 0:
            raise ValueError
    except ValueError:
        exit(-1)
    if n == 1:
        return False
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        while tmp*tmp <= n:
            if n % tmp == 0:
                return False
            tmp += 2
        return True


def get_simple(n):
    cnt = 1
    num = 3
    try:
        if int(n) <= 0:
            raise ValueError
    except ValueError:
        exit(-1)
    if n == 1:
        return 2
    while True:
        if is_simple(num):
            cnt += 1
            if cnt == n:
                return num
        num += 2


def eratos(n):
    simples = [2]
    cnt = 1
    num = 1
    try:
        if int(n) <= 0:
            raise ValueError
    except ValueError:
        exit(-1)
    if n == 1:
        return 2
    while True:
        flag = False
        num += 2
        for i in simples:
            if i * i > num:
                break
            if num % i == 0:
                flag = True
                break
        if flag:
            continue
        else:
            simples.append(num)
            cnt += 1
            if cnt == n:
                return simples[-1]


#print(get_simple(1000))
#print(eratos(1000))

print(timeit.timeit("get_simple(N)", setup="from __main__ import get_simple, N", number=1000))
print(timeit.timeit("eratos(N)", setup="from __main__ import eratos, N", number=1000))
