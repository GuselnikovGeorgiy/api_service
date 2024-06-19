from typing import Optional

from pydantic import BaseModel, Field, IPvAnyAddress
from datetime import datetime


class GeoPosition(BaseModel):
    latitude: float
    longitude: float


class TimeOnPage(BaseModel):
    page_url: str
    time_spent: int  # время, проведенное на странице в секундах


class UserDataInsert(BaseModel):
    ip_address: IPvAnyAddress | None = Field(..., description="IP")
    user_agent: str | None = Field(..., description="User Agent")
    screen_resolution: str | None = Field(..., description="Разрешение экрана")
    window_resolution: str | None = Field(..., description="Разрешение окна браузера")
    dots_per_inch: int | None = Field(..., description="Точек на дюйм (DPI)")
    os_info: str | None = Field(..., description="Операционная система")
    geo_position: Optional[GeoPosition] | None = Field(None, description="Геопозиция")
    cookies: dict | None = Field(..., description="Информация из cookie")
    connect_time: datetime | None = Field(..., description="Время подключения")
    disconnect_time: datetime | None = Field(..., description="Время отключения")
    page_views: list[TimeOnPage] | None = Field(..., description="Время, проведенное на странице")
    navigation_history: list[str] | None = Field(..., description="История переходов между страницами")


class UserDataGet(UserDataInsert):
    connection_duration: Optional[int | None] = Field(None, description="Продолжительность подключения в секундах")


# Пример JSON для записи
example_data = {
    "ip_address": "192.168.0.1",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "screen_resolution": "1920x1080",
    "window_resolution": "1024x768",
    "dots_per_inch": 96,
    "os_info": "Windows 10",
    "geo_position": {
        "latitude": 55.7558,
        "longitude": 37.6176
    },
    "cookies": {
        "session_id": "abc123",
        "preferences": {
            "theme": "dark"
        }
    },
    "connect_time": "2023-01-01T12:00:00",
    "disconnect_time": "2023-01-01T13:00:00",
    "page_views": [
        {
            "page_url": "https://example.com/home",
            "time_spent": 300
        },
        {
            "page_url": "https://example.com/about",
            "time_spent": 200
        }
    ],
    "navigation_history": [
        "https://example.com/home",
        "https://example.com/about",
        "https://example.com/contact"
    ]
}
