# Generated by Django 2.2.6 on 2020-01-08 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_auto_20200105_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='premium_accout',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='please_specify_food_perference',
            field=models.IntegerField(blank=True, choices=[(1, 'VEG'), (2, 'NONVEG'), (3, 'VEG/NONVEG')], null=True),
        ),
    ]
