from datetime import datetime

class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.wines = {wine.title: wine for (wine) in wines}
        self.beers = {beer.title: beer for (beer) in beers}
        self.drinks = self.wines | self.beers

    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)

        :param title:
        :return: True|False
        """
        return title in self.drinks

    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        return sorted(self.drinks)

    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        result = []

        try:
            from_date = datetime.strptime(from_date, "%d.%m.%Y").date()
            to_date = datetime.strptime(to_date, "%d.%m.%Y").date()
        except:
            return result

        for drink in self.drinks.values():
            if drink.production_date and from_date <= drink.production_date <= to_date:
                result.append(drink.title)

        return result

