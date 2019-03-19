class MakeCake:
    def __init__(self):
        self.recipes = dict()
        self.products = dict()
        self.cakes = dict()

    def add_recipe(self, recipes: dict):
        for k, v in recipes.items():
            self.recipes[k] = v

    def print_recipes(self):
        for recipe_name, prod_dict in self.recipes.items():
            print(f"{recipe_name}:")
            for product, number in prod_dict.items():
                print(f"{product}: {number}")

    def add_products(self, products: dict):
        for k, v in products.items():
            if k in self.products.keys():
                self.products[k] += v
            else:
                self.products[k] = v

    def print_products(self):
        for k, v in self.products.items():
            print(f"{k}: {v}")
        print()

    def print_cakes(self):
        for k, v in self.cakes.items():
            print(f"{k}: {v}")

    def make_cake(self, caketype: str):
        if caketype in self.recipes.keys():
            if len(self.need_buy(self.recipes[caketype])) == 0:
                for k, v in self.recipes[caketype].items():
                    self.products[k] -= v
                if caketype not in self.cakes:
                    self.cakes[caketype] = 1
                else:
                    self.cakes[caketype] += 1
            else:
                print(f"Необходимо купить {self.need_buy(self.recipes[caketype])}")
        else:
            print("Нет такого рецепта")

    def need_buy(self, needprod: dict):
        res = dict()
        for k, v in needprod.items():
            if k not in self.products.keys():
                res[k] = v
            else:
                if v > self.products[k]:
                    res[k] = v - self.products[k]
        return res


my_recipes = {"Торт сливочный": {"Мука": 10, "Сливки": 12, "Масло": 6},
              "Торт ягодный": {"Мука": 9, "Ягоды": 15, "Масло": 5},
              "Торт со сгущенкой": {"Мука": 8, "Сгущеное молоко": 7, "Масло": 5}}

prod_set1 = {"Мука": 10, "Ягоды": 10, "Масло": 10}
prod_set2 = {"Мука": 12, "Сливки": 10, "Сгущеное молоко": 10}
prod_set3 = {"Ягоды": 5, "Масло": 1}

cook1 = MakeCake()
cook1.add_recipe(my_recipes)
#cook1.print_recipes()
#cook1.print_products()
cook1.add_products(prod_set1)
cook1.add_products(prod_set2)
#cook1.print_products()
cook1.add_products(prod_set2)
cook1.print_products()
cook1.make_cake("Торт сливочный")
cook1.add_products(prod_set3)
cook1.make_cake("Торт ягодный")
cook1.print_products()
cook1.print_cakes()
