# Generated by Django 2.2.6 on 2020-01-05 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_profile_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='nature_of_institution',
            field=models.IntegerField(blank=True, choices=[(1, 'CATRER'), (2, 'COMPANY'), (3, 'COLLEGE'), (4, 'SCHOOL'), (5, 'FACTORY'), (6, 'HOSTEL')], null=True),
        ),
    ]
