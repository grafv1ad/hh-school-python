from datetime import datetime

class Drink:
    def __init__(self, title=None, production_date=None) -> None:
        self.title = title
        try:
            self.production_date = datetime.strptime(production_date, "%d.%m.%Y").date()
        except:
            self.production_date = None
