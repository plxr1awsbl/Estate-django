# Generated by Django 4.2.7 on 2023-12-11 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_property_bathrooms_alter_property_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='bathrooms',
            field=models.PositiveSmallIntegerField(default=2),
        ),
    ]
