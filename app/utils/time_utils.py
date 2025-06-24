from datetime import datetime
from zoneinfo import ZoneInfo

TZ_LIMA = ZoneInfo("America/Lima")

def get_now_lima() -> datetime:
    return datetime.now(TZ_LIMA)

def get_today_lima() -> datetime.date:
    return get_now_lima().date()