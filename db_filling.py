import csv
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fogstream.settings")
import django
django.setup()
from cities.models import City


with open('city.csv') as f:
  rows = csv.DictReader(f)
  for row in rows:
    _, created = City.objects.get_or_create(
      address=row.get('address'),
      postal_code=row.get('postal_code'),
      country=row.get('country'),
      federal_district=row.get('federal_district'),
      region_type=row.get('region_type'),
      region=row.get('region'),
      area_type=row.get('area_type'),
      area=row.get('area'),
      city_type=row.get('city_type'),
      city=row.get('city'),
      settlement_type=row.get('settlement_type'),
      settlement=row.get('settlement'),
      kladr_id=row.get('kladr_id'),
      fias_id=row.get('fias_id'),
      fias_level=row.get('fias_level'),
      capital_marker=row.get('capital_marker'),
      okato=row.get('okato'),
      oktmo=row.get('oktmo'),
      tax_office=row.get('tax_office'),
      timezone=row.get('timezone'),
      geo_lat=row.get('geo_lat'),
      geo_lon=row.get('geo_lon'),
      population=row.get('population'),
      foundation_year=row.get('foundation_year')
    )
