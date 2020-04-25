import json
import pprint

import requests


class VstupInfo:
    def __init__(self):
        self._main_api_url = 'https://registry.edbo.gov.ua/api'
        self._universities_api_params = {
            'ut': 'high',
            'exp': 'json',
            'lc': ''
        }
        self._specific_university_api_params = {
            'exp': 'json',
            'id': ''
        }
        self._regions_codes = dict()
        self._specialities = dict()
        self._basic_universities_info = list()
        self._specific_universities_info = list()

    @property
    def regions_codes(self):
        if not self._regions_codes:
            self._get_regions_codes()

        return self._regions_codes

    @property
    def basic_universities_info(self):
        if not self._regions_codes:
            self._get_regions_codes()
        if not self._basic_universities_info:
            self._get_basic_universities_info()
            with open('basic_universities_info.txt', 'w') as fl:
                json.dump(self._basic_universities_info, fl)

        return self._basic_universities_info

    @property
    def specific_universities_info(self):
        if not self._regions_codes:
            self._get_regions_codes()
        if not self._basic_universities_info:
            self._get_basic_universities_info()
            with open('basic_universities_info.txt', 'w') as fl:
                json.dump(self._basic_universities_info, fl)
        if not self._specific_universities_info:
            self._get_specific_universities_info()
            with open('specific_universities_info.txt', 'w') as fl:
                json.dump(self._specific_universities_info, fl)

        return self._specific_universities_info

    @property
    def specialities(self):
        if not self._specialities:
            self._get_specialities()

        return self._specialities

    def _get_regions_codes(self):
        import os
        os.path.abspath(__file__)
        with open('regions_codes.json', 'r', encoding='utf-8') as fl:
            self._regions_codes = json.load(fl)

    def _get_specialities(self):
        with open('specialities.json', 'r', encoding='utf-8') as fl:
            self._specialities = json.load(fl)

    def _get_basic_universities_info(self):
        for region_id, region_name in self._regions_codes.items():
            self._universities_api_params['lc'] = region_id
            self._basic_universities_info.extend(self._university_data_from_api())

    def _get_specific_universities_info(self):
        for university in self._basic_universities_info:
            self._specific_university_api_params['id'] = str(university['university_id'])
            self._specific_universities_info.append(self._university_data_from_api(is_specific=True))

    def _university_data_from_api(self, is_specific=False):

        if is_specific:
            data = requests.get(f'{self._main_api_url}/university/', params=self._specific_university_api_params)
        else:
            data = requests.get(f'{self._main_api_url}/universities/', params=self._universities_api_params)

        if 'Заклади не знайдено' in data.text:

            return list()

        return data.json()


if __name__ == '__main__':
    inf = VstupInfo()
    bui = inf.basic_universities_info
    sui = inf.specific_universities_info

    with open('specific_universities_info.txt', 'w') as fl:
        fl.write(pprint.pformat(sui))

    with open('basic_universities_info.txt', 'w') as fl:
        fl.write(pprint.pformat(bui))

    print("DONE")
