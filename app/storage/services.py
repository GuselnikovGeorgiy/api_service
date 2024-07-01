from collections import defaultdict
from datetime import datetime

from app.storage.exceptions import BadDataException
from app.storage.models import UserDataInsert


def validate_ip_address(ip_address: str) -> list[str]:
    import ipaddress
    errors = []

    if ip_address:
        try:
            _ = ipaddress.ip_address(ip_address)
        except ValueError:
            errors.append("Ошибка в фильтре: IP-адрес.")
    return errors


# def validate_screen_resolution(screen_resolution: str) -> list[str]:
#     import re
#     errors = []
#     pattern = re.compile(r"^\d{1,5}x\d{1,5}$")
#     if pattern.match(screen_resolution) is None:
#         errors.append("Неверно задано разрешение экрана.")
#     return errors
#
#
# def validate_window_resolution(window_resolution: str) -> list[str]:
#     import re
#     errors = []
#     pattern = re.compile(r"^\d{1,5}x\d{1,5}$")
#     if pattern.match(window_resolution) is None:
#         errors.append("Неверно задано разрешение окна.")
#     return errors

def validate_connect_time(connect_time_from: datetime, connect_time_to: datetime) -> list[str]:
    errors = []
    if connect_time_from and connect_time_to and connect_time_from > connect_time_to:
        errors.append('Ошибка в фильтре: Время подключения.')
    return errors


def validate_disconnect_time(disconnect_time_from: datetime, disconnect_time_to: datetime) -> list[str]:
    errors = []
    if disconnect_time_from and disconnect_time_to and disconnect_time_from > disconnect_time_to:
        errors.append('Ошибка в фильтре: Время отключения.')
    return errors


def connection_duration(connection_duration_from: int, connection_duration_to: int) -> list[str]:
    errors = []
    if connection_duration_from and connection_duration_to and connection_duration_from > connection_duration_to:
        errors.append('Ошибка в фильтре: Продолжительность подключения.')
    return errors


def validate_latitude(max_latitude: float, min_latitude: float) -> list[str]:
    errors = []
    if max_latitude and min_latitude:
        if max_latitude < min_latitude:
            errors.append('Ошибка в фильтре: максимальная широта должна быть больше минимальной.')
    if max_latitude and not (-90 <= max_latitude <= 90):
        errors.append('Ошибка в фильтре: максимальная широта должна быть в диапазоне от -90 до 90.')
    if min_latitude and not (-90 <= min_latitude <= 90):
        errors.append('Ошибка в фильтре: минимальная широта должна быть в диапазоне от -90 до 90.')
    return errors


def validate_longitude(max_longitude: float, min_longitude: float) -> list[str]:
    errors = []
    if max_longitude and min_longitude:
        if max_longitude < min_longitude:
            errors.append('Ошибка в фильтре: максимальная долгота должна быть больше минимальной.')
    if max_longitude and not (-180 <= max_longitude <= 180):
        errors.append('Ошибка в фильтре: максимальная долгота должна быть в диапазоне от -180 до 180.')
    if min_longitude and not (-180 <= min_longitude <= 180):
        errors.append('Ошибка в фильтре: минимальная долгота должна быть в диапазоне от -180 до 180.')
    return errors


def validate_limit(limit: int) -> list[str]:
    errors = []

    if limit is not None and limit <= 0:
        errors.append('Лимит должен быть положительным числом.')
    return errors


# def validate_dpi(ppi: int) -> list[str]:
#     errors = []
#
#     if ppi is not None and ppi <= 0:
#         errors.append('DPI должен быть положительным числом.')
#     return errors


def validate_fetch_params(
    ip_address: str | None = None,
    min_longitude: float | None = None,
    max_longitude: float | None = None,
    min_latitude: float | None = None,
    max_latitude: float | None = None,
    connect_time_from: datetime | None = None,
    connect_time_to: datetime | None = None,
    disconnect_time_from: datetime | None = None,
    disconnect_time_to: datetime | None = None,
    connection_duration_from: int | None = None,
    connection_duration_to: int | None = None,
    session_id: str | None = None,
    limit: int | None = None
) -> bool:
    errors = defaultdict(list)
    errors["ip_address"] = validate_ip_address(ip_address)
    errors["longitude"] = validate_longitude(max_longitude, min_longitude)
    errors["latitude"] = validate_latitude(max_latitude, min_latitude)
    errors["connect_time"] = validate_connect_time(connect_time_from, connect_time_to)
    errors["disconnect_time"] = validate_disconnect_time(disconnect_time_from, disconnect_time_to)
    errors["connection_duration"] = connection_duration(connection_duration_from, connection_duration_to)
    errors["limit"] = validate_limit(limit)

    error_dict = {
        field: field_errors for field, field_errors in errors.items()
        if len(field_errors) > 0
    }

    if error_dict:
        raise BadDataException(error_dict)

    return True
