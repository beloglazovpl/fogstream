# Generated by Django 4.0.4 on 2022-05-10 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0003_alter_city_foundation_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=20)),
                ('house', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Адреc',
                'verbose_name_plural': 'Адреса',
            },
        ),
    ]
