from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)


class University(models.Model):
    name = models.CharField(max_length=100, unique=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE)


class Speciality(models.Model):
    name = models.CharField(max_length=150)
    university = models.ForeignKey('University', on_delete=models.CASCADE)
