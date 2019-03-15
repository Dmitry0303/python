import math


class Triangle:
    def __init__(self, a=0, b=0, c=0):               #Конструктор класса
        try:
            self.__a = float(a)
            self.__b = float(b)
            self.__c = float(c)

            if a <= 0 or b <= 0 or c <= 0 or a >= b+c or b >= a+c or c >= a+b:
                print("Нельзя создать треугольник")
                exit(1)

        except ValueError:
            print("Неверное значение параметра")
            exit(1)

    def set_a(self, value):                         #Свойство для а
        try:
            self.__a = float(value)
            if value >= self.__b + self.__c:
                raise ValueError
        except ValueError:
            print("Неверное значение параметра")
            exit(1)

    def get_a(self):                                #Свойство для а
        return self.__a

    def set_b(self, value):                         #Свойство для b
        try:
            self.__b = float(value)
            if value >= self.__a + self.__c:
                raise ValueError
        except ValueError:
            print("Неверное значение параметра")
            exit(1)

    def get_b(self):                                #Свойство для b
        return self.__b

    def set_c(self, value):                         #Свойство для c
        try:
            self.__c = float(value)
            if value >= self.__b + self.__a:
                raise ValueError
        except ValueError:
            print("Неверное значение параметра")
            exit(1)

    def get_c(self):                                #Свойство для c
        return self.__c

    a = property(get_a, set_a)
    b = property(get_b, set_b)
    c = property(get_c, set_c)

    def get_sides(self):                            #Функция возвращения длин сторон
        return self.__a, self.__b, self.__c

    def get_p(self):                                #Функция возвращения периметра
        return self.__a + self.__b + self.__c

    def get_s(self):                                #Функция возвращения площади
        p = self.get_p()
        return math.sqrt(p*(p-self.__a)*(p-self.__b)*(p-self.__c))


triangle1 = Triangle(4, 7, 8)
print(triangle1.get_sides())
print(triangle1.get_p())
print(triangle1.get_s())
triangle1.a = 10
print(triangle1.get_sides())
print(triangle1.get_p())
print(triangle1.get_s())