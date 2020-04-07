import json
import pprint

import requests
from bs4 import BeautifulSoup


class VstupInfo:
    def __init__(self, vstup_main_url):
        self.vstup_main_url = vstup_main_url
        self.vstup_main_html = self.get_html(self.vstup_main_url)
        self.__cities = dict()
        self.__universities = dict()
        self.__specialities = dict()
        self.__parse_cities()
        self.__parse_universities()
        self.__parse_specialities()

    @property
    def cities(self):
        return self.__cities

    @property
    def universities(self):
        return self.__universities

    @property
    def specialities(self):
        return self.__specialities

    def __parse_cities(self):
        print("parsing cities...")
        cities_soup = BeautifulSoup(self.vstup_main_html, features='lxml')
        cities_tags = cities_soup.find('div', class_='image-region-select-block')\
            .find('select', class_='region-select').find_all('option')
        cities_tags.pop(0)

        self.__cities = {tag.get('value'): tag.text for tag in cities_tags}
        pprint.pprint(self.__cities)

    def __parse_universities(self):
        print('\nparsing universities...')
        for city_lnk_code in self.__cities.keys():
            self.__universities[city_lnk_code] = self.parse_universities_from_city(self.vstup_main_url + city_lnk_code)
        pprint.pprint(self.__universities)

    def __parse_specialities(self):
        print('\nparsing specialities...')
        for city_lnk_code in self.__cities.keys():
            for university in self.__universities[city_lnk_code]:
                university_lnk_code, university_name = university
                self.__specialities[university_lnk_code] = self.parse_specialities_from_university(
                    self.vstup_main_url + university_lnk_code
                )
                pprint.pprint(self.__specialities[university_lnk_code])

    def parse_universities_from_city(self, link):
        html = self.get_html(link)
        vnz_soup = BeautifulSoup(html, features='lxml')
        #vnz_vip_tags = vnz_soup.find('div', {'class': 'section-search-result'})\
        #    .find('ul', {'class': 'section-search-result-vip-list'}).find_all('a', {'class': 'search-result-item'})
        vnz_tags = vnz_soup.find('div', class_='section-search-result') \
            .find('ul', class_='section-search-result-list').find_all('a', class_='search-result-item')
        
        universities_from_city = [(tag.get('href'), tag.text) for tag in vnz_tags]

        return universities_from_city

    def parse_specialities_from_university(self, link):
        html = self.get_html(link)
        specialities_soup = BeautifulSoup(html, features='lxml')

        specialities_table_tags = specialities_soup.find('div', class_='table-of-specs')\
            .select('div.row.no-gutters.table-of-specs-item-row.qual1.base40')

        specialities_tags = [
            tag.find('div', class_='table-of-specs-item')\
                .find('span', class_='search')\
                    .find('b', text='Спеціальність:')\
                        # TODO: change this to child
                        .find_next_sibling('a') for tag in specialities_table_tags
        ]

        specialities_from_university = [(tag.get('href'), tag.text) for tag in specialities_tags]

        return specialities_from_university

    def get_html(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
        }
        html = requests.get(url, headers=headers)
        html.encoding = 'utf-8'

        return html.text


if __name__ == '__main__':
    info = VstupInfo('https://vstup.osvita.ua/')

    pprint.pprint(info.universities)