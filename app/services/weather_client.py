import os
from typing import Tuple, Dict, Any

import requests
from dotenv import load_dotenv

GEO_URL = "https://api.openweathermap.org/geo/1.0/direct"
ONE_CALL_URL = "https://api.openweathermap.org/data/3.0/onecall"


class WeatherClient:
    def __init__(self) -> None:
        load_dotenv()
        api_key = os.getenv("OPENWEATHERMAP_API_KEY")
        if not api_key:
            raise RuntimeError(
                "OPENWEATHERMAP_API_KEY is not set in the environment.")
        self.api_key = api_key

    def city_to_lat_lon(self, city: str) -> Tuple[float, float]:
        """Convert city name to (lat, lon) using the OpenWeatherMap Geocoding API."""
        resp = requests.get(
            GEO_URL,
            params={"q": city, "limit": 1, "appid": self.api_key},
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()
        if not data:
            raise ValueError(f"No location found for: {city}")
        return data[0]["lat"], data[0]["lon"]

    def get_weather(self, city: str, units: str = "metric") -> Dict[str, Any]:
        """Resolve city to lat/lon and fetch current weather (including UV index)."""
        lat, lon = self.city_to_lat_lon(city)
        resp = requests.get(
            ONE_CALL_URL,
            params={
                "lat": lat,
                "lon": lon,
                "appid": self.api_key,
                "units": units,
                "exclude": "minutely,daily,alerts",
            },
            timeout=10,
        )
        resp.raise_for_status()
        return resp.json()
