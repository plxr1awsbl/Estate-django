# Generated by Django 4.2.7 on 2023-12-22 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0021_propertyimage_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='project',
            field=models.CharField(default=None, help_text='Project that owns the property', max_length=20, null=True),
        ),
    ]
