from wine import Wine
from beer import Beer
from market import Market

wines = [
    Wine("vino", "01.01.2001"),
    Wine("vino2", "01.01.2002"),
]

beers = [
    Beer("pivo", "02.01.2001"),
    Beer("pivo2", "01.01.2003"),
]

market = Market(wines, beers)
# market = Market([], [])

print(market.has_drink_with_title("vino")) # True
print(market.has_drink_with_title("pivo")) # True
print(market.has_drink_with_title("test")) # False

print("-----")

sorted_drinks = market.get_drinks_sorted_by_title()
for i, drink in enumerate(sorted_drinks):
    print(f"{i + 1}. {drink}") # Drink title TODO

print("-----")

drinks_by_date = market.get_drinks_by_production_date("01.01.2001", "01.01.2003")
for i, drink in enumerate(drinks_by_date):
    print(f"{i + 1}. {drink}") # Drink title TODO

"""
TODO: Доработать заготовки классов вина (Wine), пива (Beer) и магазина (Market) таким образом, чтобы через класс Market можно было:

    * (*) написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
"""
