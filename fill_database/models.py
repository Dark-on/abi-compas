from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)


class University(models.Model):
    name = models.CharField(max_length=255, unique=True)
    site = models.CharField(max_length=200)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    specializations = models.ManyToManyField('Speciality', through='Specialization')


class Specialization(models.Model):
    university = models.ForeignKey('University', on_delete=models.CASCADE)
    speciality = models.ForeignKey('Speciality', on_delete=models.CASCADE)
    specialization_name = models.CharField(max_length=200, null=True)


class Speciality(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50, null=True, unique=True)