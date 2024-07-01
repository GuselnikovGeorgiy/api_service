from datetime import datetime

from fastapi import Query
from pydantic import BaseModel, Field


class UserDataFilter(BaseModel):
    ip_address: str | None = Field(
        Query(None,
              description="IP-адрес (192.168.0.1)")
    )
    user_agent: str | None = Field(
        Query(None,
              description="User Agent (Mozilla/Chrome/Safari)")
    )
    os_info: str | None = Field(
        Query(None,
              description="Операционная система (Windows 10/Linux)")
    )
    min_latitude: float | None = Field(
        Query(None,
              description="Минимальная широта (37.3456)")
    )
    max_latitude: float | None = Field(
        Query(None,
              description="Максимальная широта (55.7558)")
    )
    min_longitude: float | None = Field(
        Query(None,
              description="Минимальная долгота (37.6176)")
    )
    max_longitude: float | None = Field(
        Query(None,
              description="Максимальная долгота (55.7558)")
    )
    connect_time_from: datetime | None = Field(
        Query(None,
              description="Время подключения от: (Формат YYYY-MM-DD HH:MM:SS)")
    )
    connect_time_to: datetime | None = Field(
        Query(None,
              description="Время подключения до: (Формат YYYY-MM-DD HH:MM:SS)")
    )
    disconnect_time_from: datetime | None = Field(
        Query(None,
              description="Время отключения от: (Формат YYYY-MM-DD HH:MM:SS)")
    )
    disconnect_time_to: datetime | None = Field(
        Query(None,
              description="Время отключения до: (Формат YYYY-MM-DD HH:MM:SS)")
    )
    connection_duration_from: int | None = Field(
        Query(None,
              description="Продолжительность подключения (в секундах) от:", ge=1)
    )
    connection_duration_to: int | None = Field(
        Query(None,
              description="Продолжительность подключения (в секундах) до:",ge=1)
    )
    session_id: str | None = Field(
        Query(None,
              description="Идентификатор сессии:")
    )
    limit: int | None = Field(
        Query(None,
              description="Максимальное количество записей:", ge=1)
    )
