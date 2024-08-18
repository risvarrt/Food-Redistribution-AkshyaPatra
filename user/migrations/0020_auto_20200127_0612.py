# Generated by Django 3.0.2 on 2020-01-27 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20200127_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='how_would_you_like_to_help',
            field=models.CharField(blank=True, choices=[('Volunteer', 'Volunteer'), ('Work On Technology Platform', 'Work On Technology Platform')], default='Veg', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nature_of_institution',
            field=models.CharField(blank=True, choices=[('CATRER', 'CATRER'), ('COMPANY', 'COMPANY'), ('COLLEGE', 'COLLEGE'), ('SCHOOL', 'SCHOOL'), ('FACTORY', 'FACTORY'), ('HOSTEL', 'HOSTEL')], default='Veg', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='please_specify_food_perference',
            field=models.CharField(blank=True, choices=[('Veg', 'Veg'), ('Non-Veg', 'Non-Veg'), ('Veg/Nonveg', 'Veg/Nonveg')], default='Veg', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status_of_registration',
            field=models.CharField(blank=True, choices=[('Veg', 'Veg'), ('Non-Veg', 'Non-Veg'), ('Veg/Nonveg', 'Veg/Nonveg')], default='Veg', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='type_of_user',
            field=models.CharField(blank=True, choices=[('Donor', 'Donor'), ('Hungers(Acceptors)', 'Hungers(Acceptors)'), ('Volunteer', 'Volunteer')], default='Veg', max_length=20, null=True),
        ),
    ]
