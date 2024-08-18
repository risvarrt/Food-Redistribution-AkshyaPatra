# Generated by Django 2.2.6 on 2020-01-07 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20200107_0355'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='volunteer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='volunteer', to='blog.Post'),
        ),
        migrations.DeleteModel(
            name='Volunteer',
        ),
    ]
