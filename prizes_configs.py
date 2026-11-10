from json_dict_processing import create_processor

# создаю конфиг для призов


CONFIG_PRIZE = {
    'prize_amount': ['prizeAmount'],
    'prize_amount_adjusted': ['prizeAmountAdjusted'],
    'award_year': (['awardYear'], int),
    'category_en': (['category', 'en']),
    'prize_status': ['prizeStatus']
}

# создаю процессор


def prize_processor():
    return create_processor(CONFIG_PRIZE, list_processor=True)
