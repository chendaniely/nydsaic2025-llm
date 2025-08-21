import requests

from chatlas import ToolRejectError
## from lat lon to weather:
# Open-Meteo no registration or key needed
# OpenWeatherMap is other API key alternative
# https://api.open-meteo.com/v1/forecast?latitude=40.7127281&longitude=-74.0060152&current_weather=true

# for testing
# lat = 40.7127281
# lon = -74.0060152

from helper.input_approval import input_approval


def get_weather(lat: float, lon: float):
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
    }

    response = requests.get(
        base_url,
        params=params,
    )

    data = response.json()

    return {k: v for k, v in data.items()}


def get_weather_check(lat: float, lon: float):
    allow = input_approval(
        "Would you like me to run the weather check function?"
    )
    if allow:
        return get_weather(lat, lon)
    raise ToolRejectError("The user has chosen to disallow the tool call.")
