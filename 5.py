##Есть список отзывов на товары. На каждой строке — по одному. Данные слегка битые, и названия товара записаны в разном регистре. 
# `id` при этом один и тот же для одного и того же товара. Перед подсчётом приведите названия к одному формату, 
# иначе они будут считаться как разные`.

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
def main():
    for i in reviews:
        i["product"] = i["product"].lower()
    print(reviews)

    aggregation = {}
    for i in reviews:
        if i["id"] not in aggregation:                 
            aggregation[i["id"]] = {"product": i["product"], "stars_total": 0, "quantity_reviews": 0, "check": 0}
        aggregation[i["id"]]["stars_total"] += i["stars"]
        aggregation[i["id"]]["quantity_reviews"] +=1
        if i["stars"] == 1 or i["stars"] ==2:
            aggregation[i["id"]]["check"] =1

    for i in aggregation:
        aggregation[i]["average_star"] = aggregation[i]["stars_total"]/aggregation[i]["quantity_reviews"]

    ##Нужно найти:

    ###- среднюю оценку каждого товара

    for i in aggregation:
        print(aggregation[i]["product"], ":", aggregation[i]["average_star"])

    ##- худший товар по средней оценке среди тех, у кого хотя бы два отзыва
    worst = None
    for i in aggregation:
        if aggregation[i]["quantity_reviews"] >= 2:
            if worst == None or aggregation[i]["average_star"]  < worst:
                worst = aggregation[i]["average_star"] 
    print(worst)

    ##- сколько отзывов на 1 или 2 звезды

    cnt_1_2 = 0
    for i in aggregation:
        if aggregation[i]["check"] ==1:
            cnt_1_2 += 1
    print(cnt_1_2)
    #- какую долю всех отзывов они составляют

    print(cnt_1_2/len(reviews))


if __name__ == '__main__':
    main()