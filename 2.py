##Дана история поисковых запросов: каждая строка — один введённый запрос. Повтор в списке значит, что этот запрос ввели ещё раз.


queries = [
    "чехол",
    "iphone",
    "чехол",
    "наушники",
    "iphone",
    "iphone",
    "кабель",
    "чехол",
    "iphone",
]


print(len(queries))
counts_queries = {}
unic_queries = list(queries)
for i in unic_queries:
    counts_queries[i] = int(queries.count(i))

##Нужно найти:

##- сколько раз ввели каждый запрос

print(counts_queries)

##- какой запрос вводили чаще всего
maximum = max(counts_queries, key = counts_queries.get)
print(maximum)

##- какую долю всех поисков он занимает

print(counts_queries[maximum]/len(queries))
ones_queres = []
for i in counts_queries:
    if counts_queries[i] == 1:
        ones_queres.append(i)

##- какие запросы встретились один раз

print(ones_queres)