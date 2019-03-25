while True:
    operation = input("Введите операцию (+, -, /, *), для выхода введите 0: ")
    if operation == '0':
        exit()
    if operation not in ('+', '-', '/', '*'):
        continue
    operand1 = float(input("Введите первый операнд: "))
    operand2 = float(input("Введите второй операнд: "))
    if operation == '+':
        result = operand1 + operand2
    elif operation == '-':
        result = operand1 - operand2
    elif operation == '/':
        if operand2 == 0:
            print("Ошибка: деление на ноль")
            continue
            result = operand1 / operand2
    elif operation == '*':
        result = operand1 * operand2
    else:
        continue
    print(f"{operand1} {operation} {operand2} = {result}")
