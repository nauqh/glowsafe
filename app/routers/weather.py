from fastapi import APIRouter, HTTPException, Query, status
import requests

from ..services.weather_client import WeatherClient

router = APIRouter(prefix="/weather", tags=["weather"])

_client = WeatherClient()


@router.get(
    "/current",
    status_code=status.HTTP_200_OK,
)
def get_current_weather(
    city: str = Query(..., description="City name, e.g. 'Melbourne'"),
) -> dict:
    """
    Get the current weather (including UV index) for a given city using OpenWeatherMap.
    """
    try:
        # Always use metric units (Celsius) for GlowSafe
        return _client.get_weather(city=city, units="metric")
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except requests.RequestException:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Unable to fetch weather data from upstream provider.",
        )
