# Generated by Django 4.2.7 on 2023-12-11 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='preview',
        ),
        migrations.AlterField(
            model_name='property',
            name='sq_mt',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]