# Generated by Django 5.0.7 on 2024-09-21 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_information_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
