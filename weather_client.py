import os
import requests
from dotenv import load_dotenv

load_dotenv()

GEO_URL = "https://api.openweathermap.org/geo/1.0/direct"
ONE_CALL_URL = "https://api.openweathermap.org/data/3.0/onecall"


class WeatherClient:
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHERMAP_API_KEY")

    def city_to_lat_lon(self, city: str) -> tuple[float, float]:
        """Convert city name to (lat, lon) using Geocoding API."""
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

    def get_weather(self, city: str, units: str = "metric") -> dict:
        """Resolve city to lat/lon, fetch current weather. Returns raw API data."""
        lat, lon = self.city_to_lat_lon(city)
        resp = requests.get(
            ONE_CALL_URL,
            params={
                "lat": lat,
                "lon": lon,
                "appid": self.api_key,
                "units": units,
                "exclude": "minutely,hourly,daily,alerts",
            },
            timeout=10,
        )
        resp.raise_for_status()
        return resp.json()


if __name__ == "__main__":
    client = WeatherClient()
    data = client.get_weather("Melbourne")
    print(data)
