# Generated by Django 4.2.7 on 2023-12-12 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_alter_propertyimage_prop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='main_photo',
        ),
    ]
