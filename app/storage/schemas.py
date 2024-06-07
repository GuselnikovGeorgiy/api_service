from datetime import datetime

from fastapi import Query
from pydantic import BaseModel, Field


class UserDataFilter(BaseModel):
    ip_address: str | None = Field(Query(None,description="IP-адрес", example="192.168.0.1"))
    user_agent: str | None = Field(Query(None, description="User Agent", example="Mozilla/Chrome/Safari"))
    os_info: str | None = Field(Query(None, description="Операционная система", example="Windows 10"))
    min_latitude: float | None = Field(Query(None, description="Минимальная широта", example="37.6176"))
    max_latitude: float | None = Field(Query(None, description="Максимальная широта", example="55.7558"))
    min_longitude: float | None = Field(Query(None, description="Минимальная долгота", example="37.6176"))
    max_longitude: float | None = Field(Query(None, description="Максимальная долгота", example="55.7558"))
    connect_time_from: datetime | None = Field(Query(None, description="Время подключения от", example="2023-01-01T12:00:00"))
    connect_time_to: datetime | None = Field(Query(None, description="Время подключения до", example="2023-01-01T13:00:00"))
    disconnect_time_from: datetime | None = Field(Query(None, description="Время отключения от", example="2023-01-01T14:00:00"))
    disconnect_time_to: datetime | None = Field(Query(None, description="Время отключения до", example="2023-01-01T15:00:00"))
    connection_duration_from: int | None = Field(Query(None, description="Продолжительность подключения от", example="300"))
    connection_duration_to: int | None = Field(Query(None, description="Продолжительность подключения до", example="600"))
    limit: int | None = Field(Query(None, description="Максимальное количество записей", ge=1, example=10))
