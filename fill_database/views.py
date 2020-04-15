import json

import requests

from info_filter.models import City, University, Speciality
from .vstup_info import VstupInfo


def update_tables(request):


    fill_cities_table(regions_codes)
    fill_universities_table(universities_info)
    # fill_specialities_table(specific_university_info)


def fill_cities_table(regions_codes):
    for region_code, region_name in regions_codes.items():
        City.objects.create(
            id=int(region_code),
            name=region_name
        )


def fill_universities_table(universities_info):
    for region_code, universities in universities_info.items():

        for university in universities:
            University.objects.create(
                id=int(university['university_id']),
                city=City.objects.filter(id=int(region_code))
            )


def fill_specialities_table(specific_university_info):

    pass
