# Generated by Django 3.0.5 on 2020-04-16 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fill_database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='speciality',
            name='code',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
