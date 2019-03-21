import random


class Game:
    def __init__(self):
        self.barrels = []
        self.comp_card = []
        self.player_card = []

    def start(self):
        self.comp_card = Game.get_card()
        self.player_card = Game.get_card()

        while True:
            print("Карточка компьютера:")
            Game.print(self.comp_card)
            print("Карточка игрока:")
            Game.print(self.player_card)
            rand_bar = random.randint(1, 90)
            while rand_bar in self.barrels:
                rand_bar = random.randint(1, 90)
            self.barrels.append(rand_bar)
            print(f"Выпал боченок №: {rand_bar}")
            if Game.is_in_card(self.comp_card, rand_bar):
                    Game.del_num(self.comp_card, rand_bar)

            while True:
                res = input("Выберете действие:\n1. Зачеркнуть\n2. Продолжить\n")
                if res == '1':
                    if Game.is_in_card(self.player_card, rand_bar):
                        Game.del_num(self.player_card, rand_bar)
                        if Game.card_is_full(self.player_card):
                            if Game.card_is_full(self.comp_card):
                                print("Ничья")
                                exit()
                            else:
                                print("Вы победили!!!")
                                exit()
                        else:
                            if Game.card_is_full(self.comp_card):
                                print("Вы проиграли")
                                exit()
                            else:
                                break
                    else:
                        print("Вы проиграли")
                        exit()
                elif res == '2':
                    if Game.is_in_card(self.player_card, rand_bar):
                        print("Вы проиграли")
                        exit()
                    else:
                        break
                else:
                    continue

    @staticmethod
    def get_card():
        card = []
        vsp = []
        for i in range(3):
            row = []
            for j in range(9):
                x = random.randint(1, 90)
                while x in vsp:
                    x = random.randint(1, 90)
                row.append(x)
                vsp.append(x)
            card.append(row)

        for row in card:
            row.sort()
            for i in range(4):
                x = random.randint(0, 8)
                while row[x] == '':
                    x = random.randint(0, 8)
                row[x] = ''
        return card

    @staticmethod
    def print(card):
        print(''.center(26, '-'))
        for row in card:
            for j in row:
                print(f"{j:2}", end=' ')
            print()
        print(''.center(26, '-'))

    @staticmethod
    def del_num(card, num):
        for row in card:
            for i in range(len(row)):
                if row[i] == num:
                    row[i] = '-'

    @staticmethod
    def is_in_card(card, num):
        for row in card:
            if num in row:
                return True
        return False

    @staticmethod
    def card_is_full(card):
        for row in card:
            for el in row:
                if el != '-' and el != '':
                    return False
        return True


a = Game()
a.start()

