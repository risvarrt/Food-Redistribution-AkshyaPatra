# Generated by Django 3.0.2 on 2020-01-27 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20200126_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='required_quntity',
            new_name='Required_Quantity',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='Meeting',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='UserName',
        ),
        migrations.AddField(
            model_name='comment',
            name='Name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='Body',
            field=models.TextField(null=True),
        ),
    ]
