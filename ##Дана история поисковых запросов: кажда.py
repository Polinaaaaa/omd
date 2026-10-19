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


##Нужно найти:

##- сколько всего поисковых запросов в ленте
##- сколько раз ввели каждый запрос
##- какой запрос вводили чаще всего
##- какую долю всех поисков он занимает
##- какие запросы встретились один раз
##

print(len(queries))
counts_queries = {}
unic_queries = list(queries)
for i in unic_queries:
    counts_queries[i] = queries.count(i)
print(counts_queries)
print(max(counts_queries, key = counts_queries.get))
print(max(counts_queries.values())/len(queries))
ones_queres = []
for i, j in counts_queries.items():
    if j == 1:
        ones_queres.append(i)
print(ones_queres)