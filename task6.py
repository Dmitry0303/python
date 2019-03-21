num = int(input("Введите номер буквы в алфавите "))
shift = ord('a')
letter = chr(num + shift - 1)
print(letter)
