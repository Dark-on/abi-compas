import requests
import json
from bs4 import BeautifulSoup


def get_html(url):
    html = requests.get(url)
    html.encoding = "utf-8"
    return html.text


def get_vnzs(link):
    html = get_html(link)
    vnz_links = list()
    vnz_names = list()
    vnz_soup = BeautifulSoup(html, features="html.parser")
    #vnz_vip_tags = vnz_soup.find("div", {"class": "section-search-result"})\
    #    .find("ul", {"class": "section-search-result-vip-list"}).find_all("a", {"class": "search-result-item"})
    vnz_tags = vnz_soup.find("div", {"class": "section-search-result"}) \
        .find("ul", {"class": "section-search-result-list"}).find_all("a", {"class": "search-result-item"})

    for tag in vnz_tags:
        vnz_links.append(tag.get("href"))
        vnz_names.append(tag.text)

    return vnz_names, vnz_links


def _main():
    data_dict = dict()
    cities = dict()
    cities_links = list()
    cities_names = list()
    vnz_names_list = list()
    vnz_links_list = list()

    vstup_main_url = "https://vstup.osvita.ua/"
    vstup_main_html = get_html(vstup_main_url)

#   ........... GET CITIES ............
    cities_soup = BeautifulSoup(vstup_main_html, features="html.parser")
    cities_tags = cities_soup.find("div", {"class": "image-region-select-block"})\
        .find("select", {"class": "region-select"}).find_all("option")
    cities_tags.pop(0)

    for tag in cities_tags:
        cities_links.append(tag.get("value"))
        cities_names.append(tag.text)
#   ........... END GET CITIES ............

    for lnk in cities_links:
        vnz_names, vnz_links = get_vnzs(vstup_main_url + lnk)
        vnz_names_list.append(vnz_names)
        vnz_links_list.append(vnz_links)

    data_dict = dict(zip(cities_names, vnz_names_list))
    print(data_dict)
    print(vnz_links_list)




if __name__ == "__main__":
    _main()
