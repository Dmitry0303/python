import os
try:
    M = int(input("Введите M: "))
    for i in range(M):
        N = int(input("Введите N: "))
        S = input("Введите S: ")
        os.system(f"python d:\\normal1.py {N} {S}")
except:
    print("Неправильный аргумент")
