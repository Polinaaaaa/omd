from prizes_configs import prize_processor
from json_dict_processing import create_processor, process_year

# создаю клнфиги для записей организаций и людей


config_person_f = {
    'id': ['id'],
    'name': (['knownName', 'en']),
    'gender': ['gender'],
    'birth_year': (['birth', 'date'], process_year),
    'country_birth': ['birth', 'place', 'country', 'en'],
    'country_now': ['birth', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], prize_processor())

}

config_org_f = {
    'id': ['id'],
    'name': (['orgName', 'en']),
    'founded_year': (['founded', 'date'], process_year),
    'country_founded': ['founded', 'place', 'country', 'en'],
    'country_now': ['founded', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], prize_processor())

}

# создаю процессоры


def person_processor():
    return create_processor(config_person_f, list_processor=False)


def org_processor():
    return create_processor(config_org_f, list_processor=False)


process_orgs = org_processor()
process_persons = person_processor()
