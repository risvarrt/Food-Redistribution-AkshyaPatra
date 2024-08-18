# Generated by Django 2.2.6 on 2020-01-05 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200105_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='availble_quantity_of_food',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='contact_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='if_any_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='if_possible_say_main_ingredients',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image_of_food',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_of_food1',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='post',
            name='pick_up_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='type_of_food',
            field=models.IntegerField(blank=True, choices=[(1, 'Cooking'), (2, 'Ready'), (3, 'On the way'), (4, 'Delivered')], null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='venue',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
