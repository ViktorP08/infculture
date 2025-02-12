money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

while money_capital >= 0:
    money_capital -= max(spend * (1 + increase) ** months - salary, 0)
    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months - 1)

