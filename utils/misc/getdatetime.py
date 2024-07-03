from datetime import datetime
import pytz

def get_date_time():
    now = datetime.now()
    timezone = pytz.timezone('Asia/Tashkent')
    local_time_with_timezone = now.astimezone(timezone)
    dt_string = local_time_with_timezone.strftime("%d/%m/%Y %H:%M:%S")

    return dt_string

def get_todys_date():
    now = datetime.now()
    timezone = pytz.timezone('Asia/Tashkent')
    local_time_with_timezone = now.astimezone(timezone)
    dt_string = local_time_with_timezone.strftime("%Y-%m-%d")
    return dt_string