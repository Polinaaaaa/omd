# считаем пустые значения по всем полям


def cnt_null(data):
    cnt_nulls = 0
    for row in data:
        for val in row:
            if row[val] is None:
                cnt_nulls += 1
    return cnt_nulls

# считаем долю пропусков


def cnt_share_null_feature(data):
    cnt_nulls = {}
    for row in data:
        for val in row:
            if val not in cnt_nulls:
                cnt_nulls[val] = [0, 0]
            cnt_nulls[val][0] += 1
            if row[val] is None:
                cnt_nulls[val][1] += 1
    for val in cnt_nulls:
        cnt_nulls[val].append(cnt_nulls[val][1]/cnt_nulls[val][0])
    return [(val, cnt_nulls[val][1], cnt_nulls[val][2]) for val in cnt_nulls]

# выводим год получения приза из даты


def years_reward(data):
    all_prizes = data.get('prizes_relevant')
    all_years = [i['award_year'] for i in all_prizes if i['award_year']
                 is not None]
    return all_years

# функция для задания из второй части, анализ данных по id


def id_checking(data):
    data = sorted(data, key=lambda i: int(i['id']))
    uniq_ids = []
    double_ids = []
    first_id = data[0]
    last_id = data[-1]

    for row in data:
        if row['id'] not in uniq_ids:
            uniq_ids.append(row['id'])
        else:
            double_ids.append(row['id'])
    double_ids = tuple(double_ids)
    return {'min_id': first_id['id'], 'min_id_dates': years_reward(first_id),
            'max_id': last_id['id'], 'max_id_dates': years_reward(last_id),
            'double_ids': double_ids}

# функция для определения разницы между соседними значениями


def gaps(data):
    ans = []
    data = sorted(data, key=lambda i: int(i['id']))
    id_list = [i.get('id') for i in data]
    for first, sec in zip(id_list, id_list[1:]):
        if int(sec)-int(first) > 1:
            ans.append((int(sec), int(first)))
    return ans
