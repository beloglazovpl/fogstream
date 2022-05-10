from django.db import models

class City(models.Model):
    address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=6, blank=True)
    country = models.CharField(max_length=20)
    federal_district = models.CharField(max_length=20)
    region_type = models.CharField(max_length=10)
    region = models.CharField(max_length=50)
    area_type = models.CharField(max_length=5, blank=True)
    area = models.CharField(max_length=50, blank=True)
    city_type = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=30, blank=True)
    settlement_type = models.CharField(max_length=10, blank=True)
    settlement = models.CharField(max_length=20, blank=True)
    kladr_id = models.CharField(max_length=13)
    fias_id = models.CharField(max_length=60)
    fias_level = models.CharField(max_length=1)
    capital_marker = models.CharField(max_length=1)
    okato = models.CharField(max_length=11, blank=True)
    oktmo = models.CharField(max_length=11, blank=True)
    tax_office = models.CharField(max_length=4, blank=True)
    timezone = models.CharField(max_length=10, blank=True)
    geo_lat = models.CharField(max_length=15)
    geo_lon = models.CharField(max_length=15)
    population = models.CharField(max_length=8)
    foundation_year = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'{self.address}'

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Address(models.Model):
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=20)
    house = models.CharField(max_length=10)
    distance = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = 'Адреc'
        verbose_name_plural = 'Адреса'
