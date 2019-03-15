class Complex:
    def __init__(self, i=0.0, j=0.0):            #Конструктор класса
        try:
            self.__i = float(i)
            self.__j = float(j)
        except ValueError:
            print("Неверное значение")
            exit(1)

    def print_comp(self):                         #Вывод комплексного числа
        print(f"i = {self.__i}, j = {self.__j}")

    def set_i(self, value):                       #Свойство для i
        try:
            self.__i = float(value)
        except ValueError:
            print("Неверное значение")
            exit(1)

    def get_i(self):                                #Свойство для i
        return self.__i

    def set_j(self, value):                         #Свойство для j
        try:
            self.__j = float(value)
        except ValueError:
            print("Неверное значение")
            exit(1)

    def get_j(self):                                #Свойство для j
        return self.__j

    i = property(get_i, set_i)
    j = property(get_j, set_j)

    def __add__(self, other):                       #Перегрузка оператора сложения
        if type(other) == Complex:
            return Complex(self.__i + other.__i, self.__j + other.__j)
        else:
            try:
                return Complex(self.__i + float(other), self.__j)
            except ValueError:
                print("Неверное значение")
                exit(1)

    def __radd__(self, other):                      #Перегрузка оператора сложения
        if type(other) == Complex:
            return Complex(self.__i + other.__i, self.__j + other.__j)
        else:
            try:
                return Complex(self.__i + float(other), self.__j)
            except ValueError:
                print("Неверное значение")
                exit(1)

    def __sub__(self, other):                       #Перегрузка оператора вычитания
        if type(other) == Complex:
            return Complex(self.__i - other.__i, self.__j - other.__j)
        else:
            try:
                return Complex(self.__i - float(other), self.__j)
            except ValueError:
                print("Неверное значение")
                exit(1)

    def __rsub__(self, other):                      #Перегрузка оператора вычитания
        if type(other) == Complex:
            return Complex(self.__i - other.__i, self.__j - other.__j)
        else:
            try:
                return Complex(float(other) - self.__i, -self.__j)
            except ValueError:
                print("Неверное значение")
                exit(1)


a = Complex(3, -5)
b = Complex(-2, 5)
c = 6 - b

c.print_comp()
