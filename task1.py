from collections import namedtuple
companies = []
Company = namedtuple('Company', ['Name', 'income1', 'income2', 'income3', 'income4'])
average = 0


def get_aver(company: Company):
    return company.income1 + company.income2 + company.income3 + company.income4


def get_aver_all(companies):
    sum = 0
    for company in companies:
        sum += get_aver(company)
    return sum/len(companies)


while True:
    try:
        n = int(input("Введите количество предприятий: "))
        if n <= 0:
            raise ValueError
        else:
            break
    except ValueError:
        print("Ошибка ввода. Введите целое положительное число")
        continue

for i in range(1, n + 1):
    name = input(f"Введите название {i}-го предприятия ")

    income1 = float(input(f"Введите прибыль {i}-го предприятия в 1-м квартале "))
    income2 = float(input(f"Введите прибыль {i}-го предприятия во 2-м квартале "))
    income3 = float(input(f"Введите прибыль {i}-го предприятия в 3-м квартале "))
    income4 = float(input(f"Введите прибыль {i}-го предприятия в 4-м квартале "))
    companies.append(Company(name, income1, income2, income3, income4))


average = get_aver_all(companies)
print(f"\nСредняя прибыль: {average}")
print("\nПредприятия с прибылью выше или равно среднему: ")
for company in companies:
    if get_aver(company) >= average:
        print(f"Компания {company.Name} заработала {get_aver(company)}")

print("\nПредприятия с прибылью ниже среднего: ")
for company in companies:
    if get_aver(company) < average:
        print(f"Компания {company.Name} заработала {get_aver(company)}")
