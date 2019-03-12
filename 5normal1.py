import sys
try:
    N = int(sys.argv[1])
    for i in range(N):
        print(sys.argv[2])
except:
    print("Неправильный аргумент")
