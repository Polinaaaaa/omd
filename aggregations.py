import statistics


def sum_values(data, feature, aggr_value):
    ans = {}
    for row in data:
        if row[aggr_value] not in ans:
            ans[row[aggr_value]] = 0
        ans[row[aggr_value]] += int(row[feature])

    ans_dict = []
    for val, cnt in ans.items():
        ans_dict.append({aggr_value: val, feature: cnt})
    return ans_dict


def cnt_values(data, aggr_value):
    ans = {}
    for row in data:
        if row[aggr_value] not in ans:
            ans[row[aggr_value]] = 0
        ans[row[aggr_value]] += 1

    ans_dict = []
    for val, cnt in ans.items():
        ans_dict.append({aggr_value: val, 'quantity': cnt})

    return ans_dict


def top_positions(data, feature, n):
    data_clear = [row for row in data if row is not None]
    top_n = sorted(data_clear, key=lambda i: i[feature], reverse=True)[:n]
    return top_n


def unique_values(data, feature):
    a = [i.get(feature) for i in data]
    a = set(a)
    return a


def mean_v(data, feature):
    a = [i.get(feature) for i in data if i.get(feature) is not None]
    return statistics.mean(a)


def median_v(data, feature):
    a = [i.get(feature) for i in data if i.get(feature) is not None]
    return statistics.median(a)


def maximum(data, feature):
    a = [i.get(feature) for i in data if i.get(feature) is not None]
    return max(a)


def minimum(data, feature):
    a = [i.get(feature) for i in data if i.get(feature) is not None]
    return min(a)
