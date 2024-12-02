import requests
from django.conf import settings


def fetch_weather(city):
    api_key = settings.ACCUWEATHER_API_KEY
    location_url = f"http://dataservice.accuweather.com/locations/v1/cities/search"
    forecast_url = f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/"

    # Fetch the location key
    location_params = {
        "apikey": api_key,
        "q": city
    }
    location_response = requests.get(location_url, params=location_params)
    location_response.raise_for_status()
    location_data = location_response.json()

    if not location_data:
        raise ValueError("City not found in AccuWeather database.")

    location_key = location_data[0]["Key"]

    # Fetch the weather forecast
    forecast_params = {
        "apikey": api_key
    }
    forecast_response = requests.get(f"{forecast_url}{location_key}", params=forecast_params)
    forecast_response.raise_for_status()
    return forecast_response.json()


def fetch_hourly_forecast(city):
    api_key = settings.ACCUWEATHER_API_KEY
    location_url = "http://dataservice.accuweather.com/locations/v1/cities/search"
    hourly_forecast_url = "http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/"

    # Fetch the location key
    location_params = {
        "apikey": api_key,
        "q": city
    }
    location_response = requests.get(location_url, params=location_params)
    location_response.raise_for_status()
    location_data = location_response.json()

    if not location_data:
        raise ValueError("City not found in AccuWeather database.")

    location_key = location_data[0]["Key"]

    # Fetch the hourly forecast
    hourly_forecast_params = {
        "apikey": api_key
    }
    hourly_forecast_response = requests.get(f"{hourly_forecast_url}{location_key}", params=hourly_forecast_params)
    hourly_forecast_response.raise_for_status()
    return hourly_forecast_response.json()


def fetch_minute_cast(city):
    api_key = settings.ACCUWEATHER_API_KEY
    location_url = "http://dataservice.accuweather.com/locations/v1/cities/search"
    minute_cast_url = "http://dataservice.accuweather.com/forecasts/v1/minute/1hour/"

    # Fetch the location key
    location_params = {
        "apikey": api_key,
        "q": city
    }
    location_response = requests.get(location_url, params=location_params)
    location_response.raise_for_status()
    location_data = location_response.json()

    if not location_data:
        raise ValueError("City not found in AccuWeather database.")

    location_key = location_data[0]["Key"]

    # Fetch the minute-by-minute precipitation data
    minute_cast_params = {
        "apikey": api_key
    }
    minute_cast_response = requests.get(f"{minute_cast_url}{location_key}", params=minute_cast_params)
    minute_cast_response.raise_for_status()
    return minute_cast_response.json()


def get_radar_map_url(location_key):
    return f"https://www.accuweather.com/en/us/national/weather-radar?locationKey={location_key}"


