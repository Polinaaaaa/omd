def counter(iter):
    cnt = {}
    for i in iter:
        cnt[i] = cnt.get(i, 0) + 1
    return sum(1 for j in cnt.values() if j > 1)

print(counter(('one', 'two', 'one', 'three')))
