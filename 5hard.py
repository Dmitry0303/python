import os
PATH = "d:\\test"
try:
    for i in os.listdir(PATH):                      #Перебираем все элемнты в директории
        if os.path.isdir(os.path.join(PATH, i)):    #Если элемент является каталогом,
            for j in os.listdir(os.path.join(PATH, i)):        #Перебираем все элементы внутри него
                if os.path.isfile(os.path.join(PATH, i, j)):   #Если этот элемент является файлом
                    os.rename(os.path.join(PATH, i, j), os.path.join(PATH, j))  #То перемещаем его по каталогу вверх

    for i in os.listdir(PATH):
        if os.path.isdir(os.path.join(PATH, i)):
            os.rmdir(os.path.join(PATH, i))         #Удаление освобожденных каталогов

except FileNotFoundError:
    print('Директория не найдена')
