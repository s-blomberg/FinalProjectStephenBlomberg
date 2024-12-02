import requests
from django.conf import settings

def fetch_weather(city):
    api_key = settings.ACCUWEATHER_API_KEY
    base_url = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/"
    location_url = f"http://dataservice.accuweather.com/locations/v1/cities/search"

    # Get location key
    location_params = {
        "apikey": api_key,
        "q": city
    }
    location_response = requests.get(location_url, params=location_params)
    location_response.raise_for_status()
    location_key = location_response.json()[0]['Key']

    # Get weather data
    weather_params = {"apikey": api_key}
    weather_response = requests.get(f"{base_url}{location_key}", params=weather_params)
    weather_response.raise_for_status()
    return weather_response.json()
