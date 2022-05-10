# Generated by Django 4.0.4 on 2022-05-09 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('postal_code', models.CharField(blank=True, max_length=6)),
                ('country', models.CharField(max_length=20)),
                ('federal_district', models.CharField(max_length=20)),
                ('region_type', models.CharField(max_length=10)),
                ('region', models.CharField(max_length=50)),
                ('area_type', models.CharField(blank=True, max_length=5)),
                ('area', models.CharField(blank=True, max_length=50)),
                ('city_type', models.CharField(blank=True, max_length=10)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('settlement_type', models.CharField(blank=True, max_length=10)),
                ('settlement', models.CharField(blank=True, max_length=20)),
                ('kladr_id', models.CharField(max_length=13)),
                ('fias_id', models.CharField(max_length=60)),
                ('fias_level', models.CharField(max_length=1)),
                ('capital_marker', models.CharField(max_length=1)),
                ('okato', models.CharField(blank=True, max_length=11)),
                ('oktmo', models.CharField(blank=True, max_length=11)),
                ('tax_office', models.CharField(blank=True, max_length=4)),
                ('timezone', models.CharField(blank=True, max_length=10)),
                ('geo_lat', models.CharField(max_length=15)),
                ('geo_lon', models.CharField(max_length=15)),
                ('population', models.CharField(max_length=8)),
                ('foundation_year', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
    ]