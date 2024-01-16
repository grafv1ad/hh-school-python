from datetime import datetime

def string_to_date(string=None) -> datetime:
    try:
        return datetime.strptime(string, "%d.%m.%Y").date()
    except:
        return None
