
# Есть статистика за пять дней работы магазина. У каждого дня число заказов,
# выручка и число возвратов.

def main():
    days = [
        {'day': 'пн', 'orders': 20, 'revenue': 40_000, 'returns': 2},
        {'day': 'вт', 'orders': 16, 'revenue': 19_200, 'returns': 4},
        {'day': 'ср', 'orders': 25, 'revenue': 55_000, 'returns': 1},
        {'day': 'чт', 'orders': 10, 'revenue': 12_000, 'returns': 3},
        {'day': 'пт', 'orders': 30, 'revenue': 48_000, 'returns': 3},
    ]

    sum_revenue = 0
    for day in days:
        sum_revenue += day['revenue']

    # Нужно найти:

    # выручку за всю неделю

    print(sum_revenue)
    maximum = -1
    for day in days:
        if day['revenue'] > maximum:
            maximum = day['revenue']
            date_maximum = day['day']

    # день с самой большой выручкой

    print(date_maximum)

    average_revenue = {}
    for day in days:
        average_revenue[day['day']] = day['revenue'] / day['orders']

    # среднюю выручку на один заказ в каждый день

    print(average_revenue)

    many_returns = []
    for day in days:
        if day['returns'] > 0.2 * day['orders']:
            many_returns.append(day['day'])

    # дни, где возвратов больше 20% заказов

    print(many_returns)


if __name__ == '__main__':
    main()
