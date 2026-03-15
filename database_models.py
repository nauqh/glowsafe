from __future__ import annotations
from datetime import UTC, datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

class WeatherRecord(Base):
    __tablename__ = "weather_records"
    # Primary key — auto-incrementing so you keep full history per city
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    # City
    city: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    # Location
    lat: Mapped[float] = mapped_column(nullable=False)
    lon: Mapped[float] = mapped_column(nullable=False)
    timezone: Mapped[str] = mapped_column(String(100), nullable=False)
    timezone_offset: Mapped[int] = mapped_column(nullable=False)
    # Timestamps (Unix)
    dt: Mapped[int] = mapped_column(nullable=False)
    sunrise: Mapped[int] = mapped_column(nullable=False)
    sunset: Mapped[int] = mapped_column(nullable=False)
    # Conditions
    temp: Mapped[float] = mapped_column(nullable=False)
    feels_like: Mapped[float] = mapped_column(nullable=False)
    pressure: Mapped[int] = mapped_column(nullable=False)
    humidity: Mapped[int] = mapped_column(nullable=False)
    dew_point: Mapped[float] = mapped_column(nullable=False)
    uvi: Mapped[float] = mapped_column(nullable=False)
    clouds: Mapped[int] = mapped_column(nullable=False)
    visibility: Mapped[int] = mapped_column(nullable=False)
    wind_speed: Mapped[float] = mapped_column(nullable=False)
    wind_deg: Mapped[int] = mapped_column(nullable=False)
    # Weather condition (first item from the weather[] array)
    weather_id: Mapped[int] = mapped_column(nullable=False)
    weather_main: Mapped[str] = mapped_column(String(100), nullable=False)
    weather_description: Mapped[str] = mapped_column(String(255), nullable=False)
    weather_icon: Mapped[str] = mapped_column(String(10), nullable=False)

class Recommendations(Base):
    __tablename__ = "recommendations"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    # User profile (LLM input)
    skin_type_id: Mapped[str] = mapped_column(String(10), nullable=False)
    location_id: Mapped[str] = mapped_column(String(100), nullable=False)
    uv_risk_level: Mapped[str] = mapped_column(String(50), nullable=False)
    burn_history: Mapped[str] = mapped_column(String(50), nullable=False)
    work_pattern: Mapped[str] = mapped_column(String(50), nullable=False)
    peak_sun_exposure: Mapped[str] = mapped_column(String(50), nullable=False)
    sunscreen_frequency: Mapped[str] = mapped_column(String(50), nullable=False)
    activity_ids: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=False)
    protection_habits: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=False)
    # LLM output
    response_text: Mapped[str] = mapped_column(Text, nullable=False)
