# Generated by Django 3.0.5 on 2020-04-16 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_filter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speciality',
            name='university',
        ),
        migrations.RemoveField(
            model_name='university',
            name='city',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Speciality',
        ),
        migrations.DeleteModel(
            name='University',
        ),
    ]
