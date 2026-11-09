# Есть список отзывов на товары. На каждой строке — по одному.
# Данные слегка битые, и названия товара записаны в разном регистре.
# `id` при этом один и тот же для одного и того же товара.
# Перед подсчётом приведите названия к одному формату,
# иначе они будут считаться как разные`.

def main():

    reviews = [
        {"id": 1, "product": "Чехол", "stars": 5},
        {"id": 1, "product": "Чехол", "stars": 3},
        {"id": 1, "product": "Чехол", "stars": 4},
        {"id": 2, "product": "Наушники", "stars": 2},
        {"id": 2, "product": "наушники", "stars": 2},
        {"id": 2, "product": "НАУШНИКИ", "stars": 5},
        {"id": 3, "product": "Планшет", "stars": 5},
        {"id": 4, "product": "Колонка", "stars": 4},
        {"id": 4, "product": "Колонка", "stars": 4},
        {"id": 5, "product": "Кабель", "stars": 1},
    ]

    for review in reviews:
        review["product"] = review["product"].lower()

    aggregation = {}
    for review in reviews:
        if review["id"] not in aggregation:
            aggregation[review["id"]] = {"product": review["product"],
                                         "stars_total": 0,
                                         "quantity_reviews": 0,
                                         "check": 0}
        aggregation[review["id"]]["stars_total"] += review["stars"]
        aggregation[review["id"]]["quantity_reviews"] += 1
        if review["stars"] == 1 or review["stars"] == 2:
            aggregation[review["id"]]["check"] = 1

    for aggr in aggregation:
        aggregation[aggr]["average_star"] = aggregation[aggr]["stars_total"] / aggregation[aggr]["quantity_reviews"]

    # Нужно найти:

    # среднюю оценку каждого товара

    for aggr in aggregation:
        print(
            aggregation[aggr]["product"], ":",
            aggregation[aggr]["average_star"]
        )

    # худший товар по средней оценке среди тех, у кого хотя бы два отзыва

    worst = None
    worst_product = None
    for i in aggregation:
        if aggregation[i]["quantity_reviews"] >= 2:
            if worst is None or aggregation[i]["average_star"] < worst:
                worst = aggregation[i]["average_star"]
                worst_product = aggregation[i]["product"]

    print(worst_product)

    # сколько отзывов на 1 или 2 звезды

    cnt_1_2 = 0
    for review in reviews:
        if review["stars"] == 1 or review["stars"] == 2:
            cnt_1_2 += 1
    print(cnt_1_2)

    # какую долю всех отзывов они составляют

    print(cnt_1_2 / len(reviews))


if __name__ == '__main__':
    main()
