from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class CookieLog:
    cookie: str
    timestamp: datetime
