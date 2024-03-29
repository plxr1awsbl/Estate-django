# Generated by Django 4.2.7 on 2023-11-26 15:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('estate_id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this Estate', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('preview', models.ImageField(upload_to='images')),
                ('price', models.PositiveIntegerField(null=True)),
                ('sq_mt', models.PositiveSmallIntegerField()),
                ('floors', models.PositiveSmallIntegerField()),
                ('bedrooms', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Properties',
            },
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images', verbose_name='Image')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='catalog.property', verbose_name='Property')),
            ],
        ),
    ]
