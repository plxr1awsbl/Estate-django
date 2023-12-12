# Generated by Django 4.2.7 on 2023-12-12 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_remove_property_main_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimage',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='propertyimage',
            name='prop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='catalog.property'),
        ),
    ]
