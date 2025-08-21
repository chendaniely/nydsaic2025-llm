import requests
from typing import Dict


def get_coordinates(location: str) -> Dict[str, float]:
    base_url: str = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": location,
        "format": "json",
        "limit": 1,  # only return the top result
        "addressdetails": 1,  # include detailed address info
    }

    headers = {"User-Agent": "example_weather/1.0 (daniel.chen@posit.co)"}
    response = requests.get(
        base_url,
        params=params,
        headers=headers,
    )

    data = response.json()

    lat = float(data[0]["lat"])
    lon = float(data[0]["lon"])

    return {"lat": lat, "lon": lon}


def get_coordinates_except(location: str) -> Dict[str, float]:
    base_url: str = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": location,
        "format": "json",
        "limit": 1,  # only return the top result
        "addressdetails": 1,  # include detailed address info
    }

    headers = {"User-Agent": "example_weather/1.0 (daniel.chen@posit.co)"}

    try:
        response = requests.get(
            base_url,
            params=params,
            headers=headers,
        )
        response.raise_for_status()

        data = response.json()

        if data:
            # Extract coordinates from first result
            lat = float(data[0]["lat"])
            lon = float(data[0]["lon"])
            print(
                f"Found results for '{location}'\nLatitude: {lat}\nLongitude: {lon}"
            )
            return {"lat": lat, "lon": lon}
        else:
            print(f"No results found for {location}")
            return {"lat": None, "lon": None}

    except:
        print("Ran into an error with the request")
        return {"lat": None, "lon": None}
