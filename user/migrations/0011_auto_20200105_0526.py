# Generated by Django 2.2.6 on 2020-01-05 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20200105_0517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='code_chef',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='code_forces',
            new_name='name_of_institution',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='geeks_for_geeks',
            new_name='your_role',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='department',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='hacker_earth',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='hacker_rank',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='leet_code',
        ),
        migrations.AddField(
            model_name='profile',
            name='mobile_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
