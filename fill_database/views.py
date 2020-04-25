from django.http import HttpResponse

from .models import Region, University, Speciality, Specialization
from .vstup_info import VstupInfo


def update_tables():
    info = VstupInfo()
    fill_regions_table(info.regions_codes)
    print("DONE fill_regions_table")
    fill_universities_and_specialities_tables(info.specific_universities_info)
    print("DONE fill_universities_and_specialities_tables")


def fill_regions_table(regions_codes):
    for region_code, region_name in regions_codes.items():
        Region.objects.create(
            id=int(region_code),
            name=region_name
        )


def fill_universities_and_specialities_tables(specific_universities_info):
    for university_info in specific_universities_info:
        university = University.objects.create(
            id=int(university_info['university_id']),
            name=university_info['university_name'],
            region=Region.objects.get(id=int(university_info['koatuu_id'][:2])),
        )

        for speciality_license in university_info['speciality_licenses']:
            if Speciality.objects.filter(code=speciality_license['speciality_code']):
                speciality = Speciality.objects.get(code=speciality_license['speciality_code'])
            else:
                speciality = Speciality.objects.create(
                    code=speciality_license['speciality_code'],
                    name=speciality_license['speciality_name']
                )

            Specialization.objects.create(
                specialization_name=speciality_license['specialization_name'],
                university=university,
                speciality=speciality
            )
