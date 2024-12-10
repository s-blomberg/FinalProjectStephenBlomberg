from .utils import fetch_weather, fetch_hourly_forecast
from django.shortcuts import render
import requests, logging

logger = logging.getLogger(__name__)

def weather_view(request):
    city = request.GET.get("city")
    weather_data = None
    hourly_forecast = None
    error_message = None

    if city:
        try:
            weather_data = fetch_weather(city)
            hourly_forecast = fetch_hourly_forecast(city)
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
        "city": city,
        "error_message": error_message,
    })
