# Generated by Django 5.0.7 on 2024-09-22 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_information_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='humidity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='information',
            name='temperature',
            field=models.FloatField(),
        ),
    ]