import math
from django.http import HttpResponse
from django.shortcuts import render
from fogstream.settings import token, secret
from .forms import AddressForm
from .models import City
from dadata import Dadata
import folium


def index(request):
    city = request.GET.get('city')
    street = request.GET.get('street')
    house = request.GET.get('house')
    try:
        distance = float(request.GET.get('distance', 0))
    except ValueError:
        distance = 0
    form = AddressForm()
    m = folium.Map(location=[60, 105], zoom_start=3)
    if city and street and house is not None:
        dadata = Dadata(token, secret)
        result = dadata.clean("address", f"{city} {street} {house}")
        try:
            geo_lat = float(result.get('geo_lat'))
            geo_lon = float(result.get('geo_lon'))
        except TypeError:
            return HttpResponse('You address input is invalid')
        lon1 = geo_lon - distance / abs(math.cos(math.radians(geo_lat)) * 111.0)
        lon2 = geo_lon + distance / abs(math.cos(math.radians(geo_lat)) * 111.0)
        lat1 = geo_lat - (distance / 111.0)
        lat2 = geo_lat + (distance / 111.0)
        cities = City.objects.filter(geo_lat__range=(lat1, lat2)).filter(geo_lon__range=(lon1, lon2))
        for city in cities:
            folium.Marker([city.geo_lat, city.geo_lon], tooltip='Click for more',
                          popup=f'{city.address}').add_to(m)
        folium.Marker([geo_lat, geo_lon], tooltip='Click for more',
                      popup=f'г.{city} ул.{street} д.{house}').add_to(m)
        m = m._repr_html_()
        context = {
            'm': m,
            'form': form,
        }
        return render(request, 'search/index2.html', context)
    else:
        m = m._repr_html_()
        context = {
            'm': m,
            'form': form
        }
        return render(request, 'search/index2.html', context)
