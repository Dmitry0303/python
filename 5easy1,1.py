import os
for i in range(1, 10):
    dir_path = os.path.join(os.getcwd(), f'dir{i}')
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')
