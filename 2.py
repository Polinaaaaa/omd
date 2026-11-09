# Дана история поисковых запросов: каждая строка — один введённый запрос.
# Повтор в списке значит, что этот запрос ввели ещё раз.

def main():
    queries = [
        'чехол',
        'iphone',
        'чехол',
        'наушники',
        'iphone',
        'iphone',
        'кабель',
        'чехол',
        'iphone'
    ]

    counts_queries = {}
    unique_queries = list(queries)
    for i in unique_queries:
        counts_queries[i] = int(queries.count(i))

    # Нужно найти:

    # сколько раз ввели каждый запрос

    print(counts_queries)

    # какой запрос вводили чаще всего
    maximum = max(counts_queries, key=counts_queries.get)
    print(maximum)

    # какую долю всех поисков он занимает

    print(counts_queries[maximum] / len(queries))
    ones_queries = []
    for query in counts_queries:
        if counts_queries[query] == 1:
            ones_queries.append(query)

    # какие запросы встретились один раз

    print(ones_queries)


if __name__ == '__main__':
    main()
