from helpers import string_to_date

class Drink:
    def __init__(self, title=None, production_date=None) -> None:
        self.title = title
        self.production_date = string_to_date()
