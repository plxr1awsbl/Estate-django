# Generated by Django 4.2.7 on 2023-12-11 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_rename_property_propertyimage_prop_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
