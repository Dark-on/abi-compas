import json
import pprint

import requests
from bs4 import BeautifulSoup


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }
    html = requests.get(url, headers=headers)
    html.encoding = 'utf-8'

    return html.text


def get_cities(html):
    cities_soup = BeautifulSoup(html, features='lxml')
    cities_tags = cities_soup.find('div', class_='image-region-select-block')\
        .find('select', class_='region-select').find_all('option')
    cities_tags.pop(0)

    cities = {tag.text: tag.get('value') for tag in cities_tags}

    return cities



def get_universities_in_city(link):
    html = get_html(link)
    vnz_soup = BeautifulSoup(html, features='lxml')
    #vnz_vip_tags = vnz_soup.find('div', {'class': 'section-search-result'})\
    #    .find('ul', {'class': 'section-search-result-vip-list'}).find_all('a', {'class': 'search-result-item'})
    vnz_tags = vnz_soup.find('div', class_='section-search-result') \
        .find('ul', class_='section-search-result-list').find_all('a', class_='search-result-item')
    
    vnzs = {tag.text: tag.get('href') for tag in vnz_tags}

    return vnzs


def get_universities(cities):
    # not for long time
    vstup_main_url = 'https://vstup.osvita.ua/'
    universities = {city_name: get_universities_in_city(vstup_main_url + city_lnk_code) for city_name, city_lnk_code in cities.items()}
    
    return universities


def get_specialities_in_university(link):
    html = get_html(link)
    specialities_soup = BeautifulSoup(html, features='lxml')

    specialities_table_tags = specialities_soup.find('div', class_='table-of-specs')\
        .select('div.row.no-gutters.table-of-specs-item-row.qual1.base40')

    specialities_tags = [
        tag.find('div', class_='table-of-specs-item')\
            .find('span', class_='search')\
                .find('b', text='Спеціальність:')\
                    .find_next_sibling('a') for tag in specialities_table_tags
    ]

    specs = {tag.text: tag.get('href') for tag in specialities_tags}

    return specs


def get_specialities(universities):
    # not for long time
    vstup_main_url = 'https://vstup.osvita.ua/'
    specialities = {university_name: (university_lnk_code, get_specialities_in_university(vstup_main_url + university_lnk_code)) for university_name, university_lnk_code in universities.values()}
    
    return specialities



def _main():
    vstup_main_url = 'https://vstup.osvita.ua/'
    vstup_main_html = get_html(vstup_main_url)

    cities = get_cities(vstup_main_html)
    universities = get_universities(cities)
    pprint.pprint(get_specialities(universities))


if __name__ == "__main__":
    _main()
