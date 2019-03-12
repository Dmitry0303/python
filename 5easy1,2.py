import os
for i in range(1, 10):
    dir_path = os.path.join(os.getcwd(), f'dir{i}')
    try:
        os.rmdir(dir_path)
    except FileNotFoundError:
        print('Директория не найдена')
    except OSError:
        print('Директория не пуста')
