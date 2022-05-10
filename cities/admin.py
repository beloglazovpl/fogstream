from django.contrib import admin
from .models import City


@admin.register(City)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'federal_district', 'region', 'city', 'postal_code')
