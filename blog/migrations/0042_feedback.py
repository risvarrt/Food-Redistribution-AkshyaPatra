# Generated by Django 2.2.6 on 2020-02-27 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0041_auto_20200128_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100, null=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
