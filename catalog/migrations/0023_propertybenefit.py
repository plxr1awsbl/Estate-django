# Generated by Django 4.2.7 on 2023-12-23 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_property_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyBenefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('prop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='benefits', to='catalog.property')),
            ],
        ),
    ]
