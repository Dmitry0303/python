recipe = {'Картофель': 5, 'Лук': 2, 'Свекла': 2, 'Перец': 1}
stock = {'Картофель': 2, 'Лук': 2, 'Свекла': 1, 'Перец': 4}
need = {}
for i in recipe.keys():
    if recipe[i] > stock[i]:
        need[i] = recipe[i] - stock[i]
if len(need) == 0:
    print("Нет необходимости в покупке")
else:
    print(f"Список необходимых для покупки продуктов: {need}")
