# Generated by Django 4.2.7 on 2023-12-23 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0023_propertybenefit'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='house_type',
            field=models.CharField(choices=[('VL', 'Villa'), ('AP', 'Appartment')], default='VL', max_length=2),
        ),
    ]
