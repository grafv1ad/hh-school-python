from datetime import datetime

def string_to_date(string=None) -> datetime:
    try:
        return datetime.strptime(string, "%d.%m.%Y").date()
    except:
        return None

def logger(function):
    def wrapper(*args, **kwargs):
        start = datetime.now().timestamp()
        print(f"function \"{function.__name__}\" started")

        result = function(*args, **kwargs)

        end = datetime.now().timestamp()
        print(f"function \"{function.__name__}\" finished execution in {end - start}ms")

        return result
    return wrapper
