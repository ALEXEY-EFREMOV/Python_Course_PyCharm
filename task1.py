money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while 1:
    money_capital+=salary
    money_capital -= spend
    spend = spend*(1+increase)
    if money_capital < 0:
        break
    month+=1


print("Количество месяцев, которое можно протянуть без долгов:", month)