# Generated by Django 3.0.2 on 2020-01-27 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_auto_20200127_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status_of_registration',
            field=models.CharField(blank=True, choices=[('Govt support entity(Registered)', 'Govt support entity(Registered)'), ('Non Govt support entity(Registered)', 'Non Govt support entity(Registered)'), ('Individual led charitable(Unregistered)', 'Individual led charitable(Unregistered)'), ('Unorganized Space(Unregistered)', 'Unorganized Space(Unregistered)'), ('Others', 'Others')], default='Govt support entity(Registered)', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='type_of_user',
            field=models.CharField(blank=True, choices=[('Donor', 'Donor'), ('Hungers(Acceptors)', 'Hungers(Acceptors)'), ('Volunteer', 'Volunteer')], default='Donor', max_length=40, null=True),
        ),
    ]
