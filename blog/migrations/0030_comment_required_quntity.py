# Generated by Django 2.2.6 on 2020-01-08 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_auto_20200108_0450'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='required_quntity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
