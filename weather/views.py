from django.shortcuts import render
from .utils import fetch_weather

def weather_view(request):
    city = request.GET.get('city', 'St. Augustine')
    weather_data = fetch_weather(city)
    return render(request, 'weather/weather.html', {'weather_data': weather_data, 'city': city})
