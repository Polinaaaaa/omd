
def extract_nested_value(obj, keys):
    obj_lowest = obj
    for key in keys:
        if key in obj_lowest and isinstance(obj_lowest, dict):
            obj_lowest = obj_lowest[key]
        else:
            return None
    return obj_lowest


def process_dictionary_with_config(dictionary, config):
    ans = {}
    for attribute, spec in config.items():
        if isinstance(spec, tuple):
            path_list = spec[0]
            function = spec[1]
        elif isinstance(spec, list):
            path_list = spec
            function = None
        else:
            raise ValueError('Тип должен быть tuple или list')
        extract_value = extract_nested_value(dictionary, path_list)
        if function is not None and extract_value is not None:
            extract_value = function(extract_value)
        ans[attribute] = extract_value
    return ans


def process_list_of_dicts_with_config(list_of_dicts, config):
    ans = []
    for i in list_of_dicts:
        ans.append(process_dictionary_with_config(i, config))
    return ans


def create_processor(config, list_processor=False):
    if list_processor:
        func = process_list_of_dicts_with_config
    else:
        func = process_dictionary_with_config

    def process(data):
        return func(data, config)
    return process


def process_year(year_string):
    if not year_string:
        return None
    year_value = year_string.split('-')[0]
    return int(year_value)


if __name__ == '__main__':
    data_test = {
        'knownName': {'en': 'Polina Gavrilova'},
        'birth': {'date': '2004-03-10'}
    }
    data_test_2 = [{
        'knownName': {'en': 'Polina Gavrilova'},
        'birth': {'date': '2004-03-10'}
    }, {
        'knownName': {'en': 'Masha NeGavrilova'},
        'birth': {'date': '2005-06-11'}
    }]

    conf_test = {
        'name': ['knownName', 'en'],
        'birth_year': (['birth', 'date'], process_year),
    }

    conf_test_2 = {
        'name': ['knownName', 'en'],
    }

    # проверка, что все получилось (валидация)

    assert process_dictionary_with_config(data_test, conf_test) == {'name': 'Polina Gavrilova', 'birth_year': 2004}
    assert process_list_of_dicts_with_config(data_test_2, conf_test) == [{'name': 'Polina Gavrilova', 'birth_year': 2004},
                                                                         {'name': 'Masha NeGavrilova', 'birth_year': 2005}]

    assert extract_nested_value(data_test,
                                ['knownName', 'en']) == 'Polina Gavrilova'
    assert extract_nested_value(data_test, ['birth', 'date']) == '2004-03-10'

    processor_test = create_processor(conf_test_2)
    assert processor_test(data_test) == {'name': 'Polina Gavrilova'}
    processor_test_2 = create_processor(conf_test, list_processor=True)
    assert processor_test_2([data_test]) == [{'name': 'Polina Gavrilova',
                                              'birth_year': 2004}]
    assert extract_nested_value(data_test, ['something', 'something']) is None

    print('Ура победа')
