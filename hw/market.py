from helpers import logger, string_to_date

class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.wines = {wine.title: wine for wine in wines if wine.title}
        self.beers = {beer.title: beer for beer in beers if beer.title}
        self.drinks = self.wines | self.beers

    @logger
    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)

        :param title:
        :return: True|False
        """
        return title in self.drinks

    @logger
    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        return sorted(self.drinks)

    @logger
    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        result = []

        from_date = string_to_date(from_date)
        to_date = string_to_date(to_date)

        if (not from_date or not to_date):
            return result

        for drink in self.drinks.values():
            if drink.production_date and from_date <= drink.production_date <= to_date:
                result.append(drink.title)

        return result
