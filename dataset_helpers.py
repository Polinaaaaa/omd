def group_by(data, feature):
    group_by = {}
    for i in data:
        values = i.get(feature)
        if values not in group_by:
            group_by[values] = []
        group_by[values].append(i)
    return group_by


def expand_items(data, item):
    ans = []
    for row in data:
        for item_v in row.get(item):
            expanded_row = {key: row.get(key) for key in row if key != item}
            expanded_row.update(item_v)
            ans.append(expanded_row)
    return ans
