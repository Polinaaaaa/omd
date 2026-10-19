
##Есть статистика за пять дней работы магазина. У каждого дня число заказов, выручка и число возвратов.


days = [
    {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
    {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
    {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
    {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
    {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
]



sum_revenue = 0
for i in days:
    sum_revenue += i["revenue"]
    
##Нужно найти:

##- выручку за всю неделю

print(sum_revenue)
maximum = -1
for i in days:
    if i["revenue"] > maximum:
        maximum = i["revenue"] 


##- день с самой большой выручкой

print(maximum)

average_revenue = {}
for i in days:
    average_revenue[i["day"]] = i["revenue"]/i["orders"]

##- среднюю выручку на один заказ в каждый день

print(average_revenue)

many_returns = []
for i in days:
    if i["returns"] > 0.2*i["orders"]:
        many_returns.append(i["day"])

##- дни, где возвратов больше 20% заказов

print(many_returns)


