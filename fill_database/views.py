import json

import requests

from abicompass_container.info_filter.models import City, University, Speciality


main_api_url = 'https://registry.edbo.gov.ua/api'
universities_api_params = {
    'ut': 'high',
    'exp': 'json',
    'lc': ''
}
specific_university_api_params = {
    'exp': 'json',
    'id': ''
}


def get_json_data(info_type, params):
    data = requests.get(f'{main_api_url}/{info_type}/', params=params)

    if 'Заклади не знайдено' in data.text:
        return None
    return data.json()


def get_regions_codes():
    with open('regions_codes.json', 'r', encoding='utf-8') as fl:
        regions_codes = json.load(fl)

    return regions_codes


def get_universities_info(regions_codes):
    universities_info = dict()
    for region_id, region_name in regions_codes.items():
        universities_api_params['lc'] = region_id
        universities_info[region_id] = get_json_data('universities', universities_api_params)

    return universities_info


def get_specific_university_info(universities_info):
    specific_university_info = dict()
    for universities_list in universities_info.values():
        if universities_list is None:
            continue
        for university in universities_list:
            univ_id = str(university['university_id'])
            specific_university_api_params['id'] = univ_id
            specific_university_info[univ_id] = get_json_data('university', specific_university_api_params)

    return specific_university_info


def update_tables():
    regions_codes = get_regions_codes()
    universities_info = get_universities_info(regions_codes)
    specific_university_info = get_specific_university_info(universities_info)

    fill_cities_table(regions_codes)
    fill_universities_table(universities_info)
    fill_specialities_table(specific_university_info)


def fill_cities_table(regions_codes):

    pass


def fill_universities_table(universities_info):

    pass


def fill_specialities_table(specific_university_info):

    pass
