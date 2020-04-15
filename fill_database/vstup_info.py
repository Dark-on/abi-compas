import json
import pprint

import requests


class VstupInfo:
    def __init__(self):
        self.main_api_url = 'https://registry.edbo.gov.ua/api'
        self.universities_api_params = {
            'ut': 'high',
            'exp': 'json',
            'lc': ''
        }
        self.specific_university_api_params = {
            'exp': 'json',
            'id': ''
        }
        # ~~~ Get region codes from file ~~~
        with open('regions_codes.json', 'r', encoding='utf-8') as fl:
            self._regions_codes = json.load(fl)
        # ~~~  ~~~
        self._basic_universities_info = list()
        self._specific_universities_info = list()

    @property
    def regions_codes(self):

        return self._regions_codes

    @property
    def basic_universities_info(self):

        if not self._basic_universities_info:
            self.get_basic_universities_info()

        return self._basic_universities_info

    @property
    def specific_universities_info(self):

        if not self._basic_universities_info:
            self.get_basic_universities_info()

        if not self._specific_universities_info:
            self.get_specific_universities_info()

        return self._specific_universities_info

    def get_basic_universities_info(self):

        for region_id, region_name in self._regions_codes.items():
            self.universities_api_params['lc'] = region_id
            # print(region_id, region_name)
            self._basic_universities_info.extend(self.university_data_from_api())

    def get_specific_universities_info(self):

        for university in self._basic_universities_info:
            self.specific_university_api_params['id'] = str(university['university_id'])
            self._specific_universities_info.append(self.university_data_from_api(is_specific=True))

    def university_data_from_api(self, is_specific=False):

        if is_specific:
            data = requests.get(f'{self.main_api_url}/university/', params=self.specific_university_api_params)
        else:
            data = requests.get(f'{self.main_api_url}/universities/', params=self.universities_api_params)

        if 'Заклади не знайдено' in data.text:
            return list()
        return data.json()


if __name__ == '__main__':
    inf = VstupInfo()

    pprint.pprint(inf.specific_universities_info)
