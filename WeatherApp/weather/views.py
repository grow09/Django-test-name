from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


# Create your views here.


def index(request):
    appid = 'ab5e673e7d5ba7389bb918dfdc0a6baa'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    cities = City.objects.all()
    all_cities = []

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    for city in cities:
        res = requests.get(url.format(city.name)).json()

        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
        }

        all_cities.append(city_info)



    context = {
        'all_info': all_cities,
        'form': form
    }

    return render(request, 'weather/index.html', context)