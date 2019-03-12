import os
dir = input("Введите директорию: ")
try:
    names = os.listdir(dir)
    for name in names:
        fullname = os.path.join(dir, name)
        print(fullname)
except FileNotFoundError:
    print("Ошибка имени директории")

