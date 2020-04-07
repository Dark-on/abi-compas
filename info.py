from pprint import pprint
import json

import requests


class VstupInfo:
    def __init__(self):
        self.main_api_url = 'https://registry.edbo.gov/api'
        self.params = {
            'ut': 'high',
            'exp': 'json',
            'lc': ''
        }
        self.__universities = ''
        with open('regions_codes.json', 'r', encoding='utf-8') as fl:
            self.regions_codes = json.load(fl)

    def get_universities(self):
        for region_code in self.regions_codes.keys():
            self.__universities[]

    def get_universities_in_region(self, region_code):
        self.params['lc'] = region_code
        return self.get_json_data(self.params)

    def get_json_data(self, params):
        data = requests.get(self.main_api_url, params=params)

        return data.json()


if __name__ == '__main__':
    vstupinfo = VstupInfo()
