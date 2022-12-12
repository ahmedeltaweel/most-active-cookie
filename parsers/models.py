from datetime import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class CookieLog:
    cookie: str
    timestamp: datetime
