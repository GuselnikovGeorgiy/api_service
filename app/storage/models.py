from pydantic import BaseModel
from datetime import datetime


class Trace(BaseModel):
    ip: str
    user_agent: str
    screen_resolution: str
    window_resolution: str
    pixel_density: str
    os: str
    geolocation: str
    cookies: str
    connection_time: datetime
    disconnect_time: datetime

