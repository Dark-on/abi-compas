# Generated by Django 3.0.5 on 2020-04-16 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fill_database', '0002_speciality_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='code',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
