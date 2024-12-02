from .utils import fetch_weather, fetch_hourly_forecast, fetch_minute_cast, get_radar_map_url
import requests
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def weather_view(request):
    city = request.GET.get("city", "St. Augustine")
    weather_data = None
    hourly_forecast = None
    minute_cast = None
    radar_map_url = None
    error_message = None

    try:
        weather_data = fetch_weather(city)
        hourly_forecast = fetch_hourly_forecast(city)
        minute_cast = fetch_minute_cast(city)
        radar_map_url = get_radar_map_url(weather_data['Headline']['EffectiveLocationKey'])
    except requests.exceptions.RequestException as e:
        error_message = "Error fetching weather data. Please try again later."
        logger.error(f"RequestException occurred: {e}")
    except ValueError as ve:
        error_message = str(ve)
        logger.error(f"ValueError occurred: {ve}")
    except Exception as ex:
        error_message = "An unexpected error occurred."
        logger.error(f"Unexpected error: {ex}")

    return render(request, "weather/weather.html", {
        "weather_data": weather_data,
        "hourly_forecast": hourly_forecast,
        "minute_cast": minute_cast,
        "radar_map_url": radar_map_url,
        "city": city,
        "error_message": error_message,
    })
